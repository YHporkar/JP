# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session, redirect, url_for
from forms import *
from models import *

app = Flask(__name__)

app.secret_key = "development-key"

page_dict = {'نمایش': 'show', 'استودیو': 'studio', 'پروژه_ها': 'projects',
             'پروژه_های_عکاسی': 'photography_projects', 'جشنواره_ها': 'festivals', 'کارشناسی_رمان': 'romance',
             'جلسات_و_کارگاه_ها': 'sessions', 'چند_رسانه_ای': 'multimedia', 'کتابخانه_انقلاب': 'enghelab_lib',
             'کتابخانه_جنگ': 'jang_lib', 'بازبینی_آثار': 'results_review', 'کارشناسی_شعر': 'poem_expert',
             'کارکرد_پلاتوها': 'plato', 'محصولات_تجسمی': 'visual_products', 'محصولات_موسیقی': 'music_products',
             'پژوهش': 'research', 'نمایشگاه_ها': 'exhibitions', 'همایش_ها': 'congress',
             'عکس_های_خریداری_شده': 'bought_photos', 'کارشناسی_آثار_مکتوب': 'letters_expert',
             'جشنواره_ها_تفصیلی': 'festivals_detailed', 'مکتوبات': 'letters', 'کتاب': 'book', 'نشریه': 'journal'}


@app.route("/")
@app.route('/index', methods=["POST", "GET"])
@app.route('/index/<error>', methods=["POST", "GET"])
def index(error=None):
    if not session.get('logged_in'):
        form = Login()
        if request.method == "POST":
            if not form.validate():
                # return "false"
                return render_template("index.html", form=form, error=error)
            else:
                if authenticate_Admin(form.username.data, form.password.data) == 1:
                    make_online(form.username.data)
                    session['user'] = form.username.data
                    session['logged_in'] = True
                    return redirect(url_for('edit_record'))
                else:
                    error = "رمز عبور اشتباه است"
        return render_template("index.html", form=form, error=error)
    return redirect(url_for('edit_record'))


@app.route("/add_record", methods=["POST", "GET"])
@app.route("/add_record/<error>", methods=["POST", "GET"])
def add_record(error=None, message=None):
    if session.get('logged_in'):
        form = adding_record()
        if request.method == "POST":
            if form.logout.data:
                make_offline(session['user'])
                session['logged_in'] = False
                session.pop('user', None)
                return redirect(url_for('index'))
            elif form.continues.data:
                session['submitted'] = 0
                session['subject'] = form.subject.data
                session['first_records'] = {'code': form.code.data, 'manager_name': form.manager_name.data,
                                            'm_s_e': form.m_s_e.data, 'm_t_e': form.m_t_e.data,
                                            'm_p_k': form.m_p_k.data,
                                            'rec_date_day': form.rec_date_day.data,
                                            'rec_date_month': form.rec_date_month.data,
                                            'rec_date_year': form.rec_date_year.data,
                                            'subject': form.subject.data}
                if form.subject.data != 'مکتوبات':
                    if auth_code(form.code.data, form.subject.data):
                        error = 'این کد قبلا ثبت شده است'
                    else:
                        for i in range(page_dict.keys().__len__()):
                            if page_dict.keys()[i] == form.subject.data:
                                return redirect(url_for(page_dict.values()[i]))
                elif form.subject.data == 'مکتوبات':
                    return redirect(url_for('letters'))
        if session.get('added'):
            message = 'گزارش با موفقیت ثبت شد'
            session['added'] = 0
        return render_template("add_record.html", this_page=session['user'], form=form, error=error, message=message)
    return redirect('index')


@app.route("/edit_record", methods=["POST", "GET"])
@app.route("/edit_record/<error>", methods=["POST", "GET"])
def edit_record(error=None, message=None):
    if session.get('logged_in'):
        form = editing_record()
        if request.method == "POST":
            if form.logout.data:
                make_offline(session['user'])
                session['logged_in'] = False
                session.pop('user', None)
                return redirect(url_for('index'))
            elif form.search.data:
                session['submitted'] = 0
                session['subject'] = form.subject.data
                if form.subject.data != 'مکتوبات':
                    if auth_code(form.code.data, form.subject.data):
                        session['code'] = form.code.data
                        for i in range(page_dict.keys().__len__()):
                            if page_dict.keys()[i] == form.subject.data:
                                return redirect(url_for('edit_'+page_dict.values()[i]))
                    elif not auth_code(form.code.data, form.subject.data):
                        error = 'هیچ گزارشی با این کد و موضوع وجود ندارد'
                elif form.subject.data == 'مکتوبات':
                    return redirect(url_for('letters'))
        if session.get('added'):
            message = 'تغییرات گزارش با موفقیت ثبت شد'
            session['added'] = 0
        return render_template("add_record - edit.html", this_page=session['user'], form=form, error=error, message=message)
    return redirect(url_for('index'))


@app.route('/search_results')
def search_results():
    if session.get('logged_in'):
        form = editing_record()
        if request.method == "POST":
            if form.logout.data:
                make_offline(session['user'])
                session['logged_in'] = False
                session.pop('user', None)
                return redirect(url_for('index'))
        return render_template("search_results.html")


@app.route("/show", methods=["POST", "GET"])
def show():
    if session.get('logged_in') and not session['submitted']:
        form = show_form()
        if request.method == "POST":
            show_record(0, session['first_records'], form.name.data, form.author.data, form.director.data,
                        form.place.data, form.salon.data, form.show_kind.data, form.frame.data,
                        form.ejra_num.data, form.contact_num.data, form.contact_status.data, form.meh_moh.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("show.html", form=form, this_page=session['user'], main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/studio", methods=["POST", "GET"])
def studio():
    if session.get('logged_in') and not session.get('submitted'):
        form = studio_form()
        if request.method == "POST":
            studio_record(0, session['first_records'], form.group_name.data, form.col_name.data, form.group_head.data,
                          form.mah_fa.data, form.using_time.data, form.famous_person.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("studio.html", form=form, this_page=session['user'], main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/projects", methods=["POST", "GET"])
def projects():
    if session.get('logged_in') and not session.get('submitted'):
        form = projects_form()
        if request.method == "POST":
            projects_record(0, session['first_records'], form.name.data, form.proj_res_name.data, form.gerd_vaz.data,
                            form.ach_vaz.data, form.pey_office.data, form.subject_description.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("projects.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/photography_projects", methods=["POST", "GET"])
def photography_projects():
    if session.get('logged_in') and not session.get('submitted'):
        form = photography_projects_form()
        if request.method == "POST":
            photography_projects_record(0, session['first_records'], form.name.data, form.photo_subject.data,
                                        form.photographer_name.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("photography_projects.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/festivals", methods=["POST", "GET"])
def festivals():
    if session.get('logged_in') and not session.get('submitted'):
        form = festivals_form()
        if request.method == "POST":
            festivals_record(0, session['first_records'], form.name.data, form.fest_subjects.data, form.level.data,
                             form.country.data, form.city.data, form.salon.data,
                             form.referee.data, form.amalkard_description.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("festivals.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/romance", methods=["POST", "GET"])
def romance():
    if session.get('logged_in') and not session.get('submitted'):
        form = bachelor_novel()
        if request.method == "POST":
            romance_record(0, session['first_records'], form.sent_asar_num.data, form.seen_asar_num.data,
                           form.short_story_num.data,
                           form.romance_num.data, form.sent_to_mehr_asar_num.data, form.sent_to_city_asar_num.data,
                           form.printed_num.data, form.in_printed_num.data, form.rejected_num.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("romance_expert.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/sessions", methods=["POST", "GET"])
def sessions():
    if session.get('logged_in') and not session.get('submitted'):
        form = sessions_form()
        if request.method == "POST":
            sessions_record(0, session['first_records'], form.name.data, form.session_subject.data, form.prof_name.data,
                            form.contact_avg.data, form.count.data, form.country.data,
                            form.city.data, form.salon.data, form.level.data, form.office.data,
                            form.achievements.data, form.meh_moh1.data, form.meh_moh2.data, form.meh_moh3.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("sessions.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/multimedia", methods=["POST", "GET"])
def multimedia():
    if session.get('logged_in') and not session.get('submitted'):
        form = multimedia_form()
        if request.method == "POST":
            multimedia_record(0, session['first_records'], form.name.data, form.frame.data, form.center.data,
                              form.used_place.data, form.producted_place.data, form.product_time.data,
                              form.used.data, form.meh_moh.data, form.description.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("multimedia.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/enghelab_lib", methods=["POST", "GET"])
def enghelab_lib():
    if session.get('logged_in') and not session.get('submitted'):
        form = library_enghelab_form()
        if request.method == "POST":
            enghelab_lib_record(0, session['first_records'], form.ex_subjects_number.data, form.ex_resource_number.data,
                                form.ex_digital_resource_number.data, form.ex_pn_resource_number.data,
                                form.lang1.data, form.lang2.data, form.lang3.data, form.new_subjects_number.data,
                                form.new_resource_number.data, form.new_digital_resource_number.data,
                                form.new_pn_resource_number.data, form.couns_pn_number.data,
                                form.couns_research_proj_number.data, form.pn_subjects_number.data,
                                form.lib_members_number.data, form.lib_members_number_thisYear.data,
                                form.lib_members_women.data, form.lib_members_men.data,
                                form.lib_members_diplom.data, form.lib_members_kardani.data,
                                form.lib_members_karshenasi.data, form.lib_members_doctori.data,
                                form.borrowed_book_number.data, form.borrowed_nash_number.data,
                                form.borrowed_digital_number.data, form.borrowed_pn_number.data,
                                form.description.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("enghelab_library.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/jang_lib", methods=["POST", "GET"])
def jang_lib():
    if session.get('logged_in') and not session.get('submitted'):
        form = library_jang_form()
        if request.method == "POST":
            jang_lib_record(0, session['first_records'], form.ex_subjects_number.data, form.ex_resource_number.data,
                            form.ex_digital_resource_number.data, form.ex_pn_resource_number.data,
                            form.lang1.data, form.lang2.data, form.lang3.data, form.new_subjects_number.data,
                            form.new_resource_number.data, form.new_digital_resource_number.data,
                            form.new_pn_resource_number.data, form.couns_pn_number.data,
                            form.couns_research_proj_number.data, form.pn_subjects_number.data,
                            form.lib_members_number.data, form.lib_members_number_thisYear.data,
                            form.lib_members_women.data, form.lib_members_men.data,
                            form.lib_members_diplom.data, form.lib_members_kardani.data,
                            form.lib_members_karshenasi.data, form.lib_members_doctori.data,
                            form.borrowed_book_number.data, form.borrowed_nash_number.data,
                            form.borrowed_digital_number.data, form.borrowed_pn_number.data,
                            form.description.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("jang_library.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/results_review", methods=["POST", "GET"])
def results_review():
    if session.get('logged_in') and not session.get('submitted'):
        form = result_review_form()
        if request.method == "POST":
            results_review_record(0, session['first_records'], form.kar_num.data, form.accepted_num.data,
                                  form.show_kind.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("result_review.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/poem_expert", methods=["POST", "GET"])
def poem_expert():
    if session.get('logged_in') and not session.get('submitted'):
        form = bachelor_poem()
        if request.method == "POST":
            poem_expert_record(0, session['first_records'], form.sent_asar.data, form.seen_asar_num.data,
                               form.collections_num.data,
                               form.one_asar_num.data, form.sent_to_mehr_asar_num.data, form.sent_to_city_asar_num.data,
                               form.printed_num.data, form.in_printed_num.data, form.rejected_num.data,
                               form.famous_persons.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("poem_expert.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/plato", methods=["POST", "GET"])
def plato():
    if session.get('logged_in') and not session.get('submitted'):
        form = plato_form()
        if request.method == "POST":
            plato_record(0, session['first_records'], form.group_name.data, form.director.data, form.name.data,
                         form.clock_num.data, form.program_kind.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("platos.html", form=form, this_page=session['user'], main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/visual_products", methods=["POST", "GET"])
def visual_products():
    if session.get('logged_in') and not session.get('submitted'):
        form = visual_products_form()
        if request.method == "POST":
            visual_products_record(0, session['first_records'], form.major_name.data, form.number.data,
                                   form.producers_name.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("visual_products.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/music_products", methods=["POST", "GET"])
def music_products():
    if session.get('logged_in') and not session.get('submitted'):
        form = music_products_form()
        if request.method == "POST":
            music_products_record(0, session['first_records'], form.music_name.data, form.outing_pos.data,
                                  form.outing_turn.data,
                                  form.frame.data, form.music_kind.data, form.singer.data,
                                  form.music_producer.data, form.tirax.data, form.meh_moh.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("music_products.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/research", methods=["POST", "GET"])
def research():
    if session.get('logged_in') and not session.get('submitted'):
        form = research_form()
        if request.method == "POST":
            research_record(0, session['first_records'], form.research_name.data, form.author.data,
                            form.research_subject.data,
                            form.outing_place.data, form.meh_moh.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("research.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/exhibitions", methods=["POST", "GET"])
def exhibitions():
    if session.get('logged_in') and not session.get('submitted'):
        form = exhibitions_form()
        if request.method == "POST":
            exhibitions_record(0, session['first_records'], form.name.data, form.show_subject.data, form.os_city.data,
                               form.city.data, form.contact_num.data, form.meh_moh.data,
                               form.finish_date_day.data, form.finish_date_month.data, form.finish_date_year.data,
                               form.description.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("exhibitions.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/congress", methods=["POST", "GET"])
def congress():
    if session.get('logged_in') and not session.get('submitted'):
        form = congress_form()
        if request.method == "POST":
            congress_record(0, session['first_records'], form.name.data, form.office.data, form.contact_num.data,
                            form.contact_pos.data, form.country.data, form.city.data,
                            form.salon.data, form.frame.data, form.meh_moh.data, form.famous_persons.data,
                            form.sokhanrans.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("congress.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/bought_photos", methods=["POST", "GET"])
def bought_photos():
    if session.get('logged_in') and not session.get('submitted'):
        form = bought_photos_form()
        if request.method == "POST":
            bought_photos_record(0, session['first_records'], form.photo_subject.data, form.number.data,
                                 form.tar_ghar.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("bought_photos.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/letters_expert", methods=["POST", "GET"])
def letters_expert():
    if session.get('logged_in') and not session.get('submitted'):
        form = bachelor_written()
        if request.method == "POST":
            letters_expert_record(0, session['first_records'], form.kar_number.data, form.accepted_number.data,
                                  form.frame.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("letters_expert.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/festivals_detailed", methods=["POST", "GET"])
def festivals_detailed():
    if session.get('logged_in') and not session.get('submitted'):
        form = festivals_detailed_form()

        if request.method == "POST":
            festivals_detailed_record(0, session['first_records'], form.name.data, form.subject.data, form.art_dab.data,
                                      form.all_asar.data, form.take_parted_person.data, form.os_city.data,
                                      form.city.data, form.finished_asar.data, form.salon.data,
                                      form.choosing_asar_team.data,
                                      form.referees.data, form.asar_parted_num.data, form.international_rec.data,
                                      form.area_rec.data, form.asar_parted_in_dif.data, form.women.data,
                                      form.men.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("festivals_detailed.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/letters", methods=["POST", "GET"])
def letters():
    if session.get('logged_in') and not session.get('submitted'):
        form = letters_form()
        if request.method == "POST":
            session['subject'] = form.result_kind.data
            if form.result_kind.data == 'کتاب':
                session['first_records']['subject'] = 'کتاب'
                return redirect(url_for('book'))
            else:
                session['first_records']['subject'] = 'نشریه'
                return redirect(url_for('journal'))

        return render_template("letters.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/book", methods=["POST", "GET"])
def book():
    if session.get('logged_in') and not session.get('submitted'):
        form = book_form()
        if request.method == "POST":
            book_record(0, session['first_records'], form.name.data, form.author.data, form.translator.data,
                        form.nasher.data, form.lang.data, form.print_turn.data,
                        form.sub_frame.data, form.roo_bar.data, form.nasher_city.data, form.meh_moh.data,
                        form.shomargan_num.data, form.pages.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("book.html", form=form, this_page=session['user'], main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/journal", methods=["POST", "GET"])
def journal():
    if session.get('logged_in') and not session.get('submitted'):
        form = journal_form()
        if request.method == "POST":
            journal_record(0, session['first_records'], form.name.data, form.head_name.data, form.print_turn.data,
                           form.shomargan_num.data, form.pages.data, form.frame.data,
                           form.roo_bar.data, form.nasher_city.data, form.festival_name.data, form.meh_moh.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("journal.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/edit_show", methods=['POST', 'GET'])
def edit_show():
    if session.get('logged_in'):
        form = show_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.author.data = select_show_record(session['code'], session['subject'])[0][9]
        form.director.data = select_show_record(session['code'], session['subject'])[0][10]
        form.place.data = select_show_record(session['code'], session['subject'])[0][11]
        form.salon.data = select_show_record(session['code'], session['subject'])[0][12]
        form.show_kind.data = select_show_record(session['code'], session['subject'])[0][13]
        form.frame.data = select_show_record(session['code'], session['subject'])[0][14]
        form.ejra_num.data = select_show_record(session['code'], session['subject'])[0][15]
        form.contact_num.data = select_show_record(session['code'], session['subject'])[0][16]
        form.contact_status.data = select_show_record(session['code'], session['subject'])[0][17]
        form.meh_moh.data = select_show_record(session['code'], session['subject'])[0][18]

        if request.method == "POST":
            show_record(1, select_first_record(session['code'], session['subject']), request.form['name'],
                        request.form["author"], request.form["director"], request.form["place"], request.form["salon"],
                        request.form["show_kind"], request.form["frame"],request.form["ejra_num"],
                        request.form["contact_num"], request.form["contact_status"], request.form["meh_moh"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("show - edit.html", form=form, this_page=session['user'], main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_studio", methods=["POST", "GET"])
def edit_studio():
    if session.get('logged_in') and not session.get('submitted'):
        form = studio_form()
        form.group_name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.col_name.data = select_show_record(session['code'], session['subject'])[0][9]
        form.group_head.data = select_show_record(session['code'], session['subject'])[0][10]
        form.mah_fa.data = select_show_record(session['code'], session['subject'])[0][11]
        form.using_time.data = select_show_record(session['code'], session['subject'])[0][12]
        form.famous_person.data = select_show_record(session['code'], session['subject'])[0][13]

        if request.method == "POST":
            studio_record(1, select_first_record(session['code'], session['subject']), request.form["group_name"], request.form["col_name"], request.form["group_head"],
                          request.form["mah_fa"], request.form["using_time"], request.form["famous_person"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("studio - edit.html", form=form, this_page=session['user'], main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_projects", methods=["POST", "GET"])
def edit_projects():
    if session.get('logged_in') and not session.get('submitted'):
        form = projects_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.proj_res_name.data = select_show_record(session['code'], session['subject'])[0][9]
        form.gerd_vaz.data = select_show_record(session['code'], session['subject'])[0][10]
        form.ach_vaz.data = select_show_record(session['code'], session['subject'])[0][11]
        form.pey_office.data = select_show_record(session['code'], session['subject'])[0][12]
        form.subject_description.data = select_show_record(session['code'], session['subject'])[0][13]

        if request.method == "POST":
            projects_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                            request.form["proj_res_name"], request.form["gerd_vaz"],
                            request.form["ach_vaz"], request.form["pey_office"], request.form["subject_description"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("projects - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_photography_projects", methods=["POST", "GET"])
def edit_photography_projects():
    if session.get('logged_in') and not session.get('submitted'):
        form = photography_projects_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.photo_subject.data = select_show_record(session['code'], session['subject'])[0][9]
        form.photographer_name.data = select_show_record(session['code'], session['subject'])[0][10]

        if request.method == "POST":
            photography_projects_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                                        request.form["photo_subject"], request.form["photographer_name"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("photography_projects - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_festivals", methods=["POST", "GET"])
def edit_festivals():
    if session.get('logged_in') and not session.get('submitted'):
        form = festivals_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.fest_subjects.data = select_show_record(session['code'], session['subject'])[0][9]
        form.level.data = select_show_record(session['code'], session['subject'])[0][10]
        form.country.data = select_show_record(session['code'], session['subject'])[0][11]
        form.city.data = select_show_record(session['code'], session['subject'])[0][12]
        form.salon.data = select_show_record(session['code'], session['subject'])[0][13]
        form.referee.data = select_show_record(session['code'], session['subject'])[0][14]
        form.amalkard_description.data = select_show_record(session['code'], session['subject'])[0][15]

        if request.method == "POST":
            festivals_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                             request.form["fest_subjects"], request.form["level"],
                             request.form["country"], request.form["city"], request.form["salon"],
                             request.form["referee"], request.form["amalkard_description"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("festivals - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_romance", methods=["POST", "GET"])
def edit_romance():
    if session.get('logged_in') and not session.get('submitted'):
        form = bachelor_novel()
        form.sent_asar_num.data = select_show_record(session['code'], session['subject'])[0][8]
        form.seen_asar_num.data = select_show_record(session['code'], session['subject'])[0][9]
        form.short_story_num.data = select_show_record(session['code'], session['subject'])[0][10]
        form.romance_num.data = select_show_record(session['code'], session['subject'])[0][11]
        form.sent_to_mehr_asar_num.data = select_show_record(session['code'], session['subject'])[0][12]
        form.sent_to_city_asar_num.data = select_show_record(session['code'], session['subject'])[0][13]
        form.printed_num.data = select_show_record(session['code'], session['subject'])[0][14]
        form.in_printed_num.data = select_show_record(session['code'], session['subject'])[0][15]
        form.rejected_num.data = select_show_record(session['code'], session['subject'])[0][16]

        if request.method == "POST":
            romance_record(1, select_first_record(session['code'], session['subject']), request.form["sent_asar_num"],
                           request.form["seen_asar_num"], request.form["short_story_num"], request.form["romance_num"],
                           request.form["sent_to_mehr_asar_num"], request.form["sent_to_city_asar_num"],
                           request.form["printed_num"], request.form["in_printed_num"], request.form["rejected_num"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("romance_expert - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_sessions", methods=["POST", "GET"])
def edit_sessions():
    if session.get('logged_in') and not session.get('submitted'):
        form = sessions_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.session_subject.data = select_show_record(session['code'], session['subject'])[0][9]
        form.prof_name.data = select_show_record(session['code'], session['subject'])[0][10]
        form.contact_avg.data = select_show_record(session['code'], session['subject'])[0][11]
        form.count.data = select_show_record(session['code'], session['subject'])[0][12]
        form.country.data = select_show_record(session['code'], session['subject'])[0][13]
        form.city.data = select_show_record(session['code'], session['subject'])[0][14]
        form.salon.data = select_show_record(session['code'], session['subject'])[0][15]
        form.level.data = select_show_record(session['code'], session['subject'])[0][16]
        form.office.data = select_show_record(session['code'], session['subject'])[0][17]
        form.achievements.data = select_show_record(session['code'], session['subject'])[0][18]
        form.meh_moh1.data = select_show_record(session['code'], session['subject'])[0][19]
        form.meh_moh2.data = select_show_record(session['code'], session['subject'])[0][20]
        form.meh_moh2.data = select_show_record(session['code'], session['subject'])[0][21]

        if request.method == "POST":
            sessions_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                            request.form["session_subject"], request.form["prof_name"],
                            request.form["contact_avg"], request.form["count"], request.form["country"],
                            request.form["city"], request.form["salon"], request.form["level"], request.form["office"],
                            request.form["achievements"], request.form["meh_moh1"], request.form["meh_moh2"], request.form["meh_moh3"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("sessions - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_multimedia", methods=["POST", "GET"])
def edit_multimedia():
    if session.get('logged_in') and not session.get('submitted'):
        form = multimedia_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.frame.data = select_show_record(session['code'], session['subject'])[0][9]
        form.center.data = select_show_record(session['code'], session['subject'])[0][10]
        form.used_place.data = select_show_record(session['code'], session['subject'])[0][11]
        form.producted_place.data = select_show_record(session['code'], session['subject'])[0][12]
        form.product_time.data = select_show_record(session['code'], session['subject'])[0][13]
        form.used.data = select_show_record(session['code'], session['subject'])[0][14]
        form.meh_moh.data = select_show_record(session['code'], session['subject'])[0][15]
        form.description.data = select_show_record(session['code'], session['subject'])[0][16]

        if request.method == "POST":
            multimedia_record(1, select_first_record(session['code'], session['subject']), request.form["name"], request.form["frame"],
                              request.form["center"],request.form["used_place"], request.form["producted_place"],
                              request.form["product_time"],request.form["used"], request.form["meh_moh"], request.form["description"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("multimedia - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_enghelab_lib", methods=["POST", "GET"])
def edit_enghelab_lib():
    if session.get('logged_in') and not session.get('submitted'):
        form = library_enghelab_form()
        form.ex_subjects_number.data = select_show_record(session['code'], session['subject'])[0][8]
        form.ex_resource_number.data = select_show_record(session['code'], session['subject'])[0][9]
        form.ex_digital_resource_number.data = select_show_record(session['code'], session['subject'])[0][10]
        form.ex_pn_resource_number.data = select_show_record(session['code'], session['subject'])[0][11]
        form.lang1.data = select_show_record(session['code'], session['subject'])[0][12]
        form.lang2.data = select_show_record(session['code'], session['subject'])[0][13]
        form.lang3.data = select_show_record(session['code'], session['subject'])[0][14]
        form.new_subjects_number.data = select_show_record(session['code'], session['subject'])[0][15]
        form.new_resource_number.data = select_show_record(session['code'], session['subject'])[0][16]
        form.new_digital_resource_number.data = select_show_record(session['code'], session['subject'])[0][17]
        form.new_pn_resource_number.data = select_show_record(session['code'], session['subject'])[0][18]
        form.couns_pn_number.data = select_show_record(session['code'], session['subject'])[0][19]
        form.couns_research_proj_number.data = select_show_record(session['code'], session['subject'])[0][20]
        form.pn_subjects_number.data = select_show_record(session['code'], session['subject'])[0][21]
        form.lib_members_number.data = select_show_record(session['code'], session['subject'])[0][22]
        form.lib_members_number_thisYear.data = select_show_record(session['code'], session['subject'])[0][23]
        form.lib_members_women.data = select_show_record(session['code'], session['subject'])[0][24]
        form.lib_members_men.data = select_show_record(session['code'], session['subject'])[0][25]
        form.lib_members_diplom.data = select_show_record(session['code'], session['subject'])[0][26]
        form.lib_members_kardani.data = select_show_record(session['code'], session['subject'])[0][27]
        form.lib_members_karshenasi.data = select_show_record(session['code'], session['subject'])[0][28]
        form.lib_members_doctori.data = select_show_record(session['code'], session['subject'])[0][29]
        form.borrowed_book_number.data = select_show_record(session['code'], session['subject'])[0][30]
        form.borrowed_nash_number.data = select_show_record(session['code'], session['subject'])[0][31]
        form.borrowed_digital_number.data = select_show_record(session['code'], session['subject'])[0][32]
        form.borrowed_pn_number.data = select_show_record(session['code'], session['subject'])[0][33]
        form.description.data = select_show_record(session['code'], session['subject'])[0][34]

        if request.method == "POST":
            enghelab_lib_record(1, select_first_record(session['code'], session['subject']),
                                request.form["ex_subjects_number"], request.form["ex_resource_number"],
                                request.form["ex_digital_resource_number"], request.form["ex_pn_resource_number"],
                                request.form["lang1"], request.form["lang2"], request.form["lang3"],
                                request.form["new_subjects_number"],
                                request.form["new_resource_number"], request.form["new_digital_resource_number"],
                                request.form["new_pn_resource_number"], request.form["couns_pn_number"],
                                request.form["couns_research_proj_number"], request.form["pn_subjects_number"],
                                request.form["lib_members_number"], request.form["lib_members_number_thisYear"],
                                request.form["lib_members_women"], request.form["lib_members_men"],
                                request.form["lib_members_diplom"], request.form["lib_members_kardani"],
                                request.form["lib_members_karshenasi"], request.form["lib_members_doctori"],
                                request.form["borrowed_book_number"], request.form["borrowed_nash_number"],
                                request.form["borrowed_digital_number"], request.form["borrowed_pn_number"],
                                request.form["description"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("enghelab_library - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_jang_lib", methods=["POST", "GET"])
def edit_jang_lib():
    if session.get('logged_in') and not session.get('submitted'):
        form = library_jang_form()
        form.ex_subjects_number.data = select_show_record(session['code'], session['subject'])[0][8]
        form.ex_resource_number.data = select_show_record(session['code'], session['subject'])[0][9]
        form.ex_digital_resource_number.data = select_show_record(session['code'], session['subject'])[0][10]
        form.ex_pn_resource_number.data = select_show_record(session['code'], session['subject'])[0][11]
        form.lang1.data = select_show_record(session['code'], session['subject'])[0][12]
        form.lang2.data = select_show_record(session['code'], session['subject'])[0][13]
        form.lang3.data = select_show_record(session['code'], session['subject'])[0][14]
        form.new_subjects_number.data = select_show_record(session['code'], session['subject'])[0][15]
        form.new_resource_number.data = select_show_record(session['code'], session['subject'])[0][16]
        form.new_digital_resource_number.data = select_show_record(session['code'], session['subject'])[0][17]
        form.new_pn_resource_number.data = select_show_record(session['code'], session['subject'])[0][18]
        form.couns_pn_number.data = select_show_record(session['code'], session['subject'])[0][19]
        form.couns_research_proj_number.data = select_show_record(session['code'], session['subject'])[0][20]
        form.pn_subjects_number.data = select_show_record(session['code'], session['subject'])[0][21]
        form.lib_members_number.data = select_show_record(session['code'], session['subject'])[0][22]
        form.lib_members_number_thisYear.data = select_show_record(session['code'], session['subject'])[0][23]
        form.lib_members_women.data = select_show_record(session['code'], session['subject'])[0][24]
        form.lib_members_men.data = select_show_record(session['code'], session['subject'])[0][25]
        form.lib_members_diplom.data = select_show_record(session['code'], session['subject'])[0][26]
        form.lib_members_kardani.data = select_show_record(session['code'], session['subject'])[0][27]
        form.lib_members_karshenasi.data = select_show_record(session['code'], session['subject'])[0][28]
        form.lib_members_doctori.data = select_show_record(session['code'], session['subject'])[0][29]
        form.borrowed_book_number.data = select_show_record(session['code'], session['subject'])[0][30]
        form.borrowed_nash_number.data = select_show_record(session['code'], session['subject'])[0][31]
        form.borrowed_digital_number.data = select_show_record(session['code'], session['subject'])[0][32]
        form.borrowed_pn_number.data = select_show_record(session['code'], session['subject'])[0][33]
        form.description.data = select_show_record(session['code'], session['subject'])[0][34]

        if request.method == "POST":
            jang_lib_record(1, select_first_record(session['code'], session['subject']), request.form["ex_subjects_number"], request.form["ex_resource_number"],
                            request.form["ex_digital_resource_number"], request.form["ex_pn_resource_number"],
                            request.form["lang1"], request.form["lang2"], request.form["lang3"], request.form["new_subjects_number"],
                            request.form["new_resource_number"], request.form["new_digital_resource_number"],
                            request.form["new_pn_resource_number"], request.form["couns_pn_number"],
                            request.form["couns_research_proj_number"], request.form["pn_subjects_number"],
                            request.form["lib_members_number"], request.form["lib_members_number_thisYear"],
                            request.form["lib_members_women"], request.form["lib_members_men"],
                            request.form["lib_members_diplom"], request.form["lib_members_kardani"],
                            request.form["lib_members_karshenasi"], request.form["lib_members_doctori"],
                            request.form["borrowed_book_number"], request.form["borrowed_nash_number"],
                            request.form["borrowed_digital_number"], request.form["borrowed_pn_number"],
                            request.form["description"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("jang_library - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_results_review", methods=["POST", "GET"])
def edit_results_review():
    if session.get('logged_in') and not session.get('submitted'):
        form = result_review_form()
        form.kar_num.data = select_show_record(session['code'], session['subject'])[0][8]
        form.accepted_num.data = select_show_record(session['code'], session['subject'])[0][9]
        form.show_kind.data = select_show_record(session['code'], session['subject'])[0][10]

        if request.method == "POST":
            results_review_record(1, select_first_record(session['code'], session['subject']),
                                  request.form["kar_num"], request.form["accepted_num"],
                                  request.form["show_kind"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("result_review - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_poem_expert", methods=["POST", "GET"])
def edit_poem_expert():
    if session.get('logged_in') and not session.get('submitted'):
        form = bachelor_poem()
        form.sent_asar.data = select_show_record(session['code'], session['subject'])[0][8]
        form.seen_asar_num.data = select_show_record(session['code'], session['subject'])[0][9]
        form.collections_num.data = select_show_record(session['code'], session['subject'])[0][10]
        form.one_asar_num.data = select_show_record(session['code'], session['subject'])[0][11]
        form.sent_to_mehr_asar_num.data = select_show_record(session['code'], session['subject'])[0][12]
        form.sent_to_city_asar_num.data = select_show_record(session['code'], session['subject'])[0][13]
        form.printed_num.data = select_show_record(session['code'], session['subject'])[0][14]
        form.in_printed_num.data = select_show_record(session['code'], session['subject'])[0][15]
        form.rejected_num.data = select_show_record(session['code'], session['subject'])[0][16]
        form.famous_persons.data = select_show_record(session['code'], session['subject'])[0][17]
        form.achievements.data = select_show_record(session['code'], session['subject'])[0][18]

        if request.method == "POST":
            poem_expert_record(1, select_first_record(session['code'], session['subject']),
                               request.form["sent_asar"], request.form["seen_asar_num"],
                               request.form["collections_num"], request.form["one_asar_num"],
                               request.form["sent_to_mehr_asar_num"], request.form["sent_to_city_asar_num"],
                               request.form["printed_num"], request.form["in_printed_num"],
                               request.form["rejected_num"], request.form["famous_persons"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("poem_expert - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_plato", methods=["POST", "GET"])
def edit_plato():
    if session.get('logged_in') and not session.get('submitted'):
        form = plato_form()
        form.group_name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.director.data = select_show_record(session['code'], session['subject'])[0][9]
        form.name.data = select_show_record(session['code'], session['subject'])[0][10]
        form.clock_num.data = select_show_record(session['code'], session['subject'])[0][11]
        form.program_kind.data = select_show_record(session['code'], session['subject'])[0][12]

        if request.method == "POST":
            plato_record(1, select_first_record(session['code'], session['subject']), request.form["group_name"],
                         request.form["director"], request.form["name"],
                         request.form["clock_num"], request.form["program_kind"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("platos - edit.html", form=form, this_page=session['user'], main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_visual_products", methods=["POST", "GET"])
def edit_visual_products():
    if session.get('logged_in') and not session.get('submitted'):
        form = visual_products_form()
        form.major_name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.number.data = select_show_record(session['code'], session['subject'])[0][9]
        form.producers_name.data = select_show_record(session['code'], session['subject'])[0][10]

        if request.method == "POST":
            visual_products_record(1, select_first_record(session['code'], session['subject']),
                                   request.form["major_name"], request.form["number"],
                                   request.form["producers_name"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("visual_products - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_music_products", methods=["POST", "GET"])
def edit_music_products():
    if session.get('logged_in') and not session.get('submitted'):
        form = music_products_form()
        form.music_name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.outing_pos.data = select_show_record(session['code'], session['subject'])[0][9]
        form.outing_turn.data = select_show_record(session['code'], session['subject'])[0][10]
        form.frame.data = select_show_record(session['code'], session['subject'])[0][11]
        form.music_kind.data = select_show_record(session['code'], session['subject'])[0][12]
        form.singer.data = select_show_record(session['code'], session['subject'])[0][13]
        form.music_producer.data = select_show_record(session['code'], session['subject'])[0][14]
        form.tirax.data = select_show_record(session['code'], session['subject'])[0][15]
        form.meh_moh.data = select_show_record(session['code'], session['subject'])[0][16]

        if request.method == "POST":
            music_products_record(1, select_first_record(session['code'], session['subject']),
                                  request.form["music_name"], request.form["outing_pos"],
                                  request.form["outing_turn"],
                                  request.form["frame"], request.form["music_kind"], request.form["singer"],
                                  request.form["music_producer"], request.form["tirax"], request.form["meh_moh"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("music_products - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_research", methods=["POST", "GET"])
def edit_research():
    if session.get('logged_in') and not session.get('submitted'):
        form = research_form()
        form.research_name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.author.data = select_show_record(session['code'], session['subject'])[0][9]
        form.research_subject.data = select_show_record(session['code'], session['subject'])[0][10]
        form.outing_place.data = select_show_record(session['code'], session['subject'])[0][11]
        form.meh_moh.data = select_show_record(session['code'], session['subject'])[0][12]

        if request.method == "POST":
            research_record(1, select_first_record(session['code'], session['subject']), request.form["research_name"],
                            request.form["author"], request.form["research_subject"],
                            request.form["outing_place"], request.form["meh_moh"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("research - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_exhibitions", methods=["POST", "GET"])
def edit_exhibitions():
    if session.get('logged_in') and not session.get('submitted'):
        form = exhibitions_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.show_subject.data = select_show_record(session['code'], session['subject'])[0][9]
        form.os_city.data = select_show_record(session['code'], session['subject'])[0][10]
        form.city.data = select_show_record(session['code'], session['subject'])[0][11]
        form.contact_num.data = select_show_record(session['code'], session['subject'])[0][12]
        form.meh_moh.data = select_show_record(session['code'], session['subject'])[0][13]
        form.finish_date_day.data = select_show_record(session['code'], session['subject'])[0][14]
        form.finish_date_month.data = select_show_record(session['code'], session['subject'])[0][15]
        form.finish_date_year.data = select_show_record(session['code'], session['subject'])[0][16]
        form.description.data = select_show_record(session['code'], session['subject'])[0][17]

        if request.method == "POST":
            exhibitions_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                               request.form["show_subject"], request.form["os_city"],
                               request.form["city"], request.form["contact_num"], request.form["meh_moh"],
                               request.form["finish_date_day"], request.form["finish_date_month"],
                               request.form["finish_date_year"], request.form["description"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("exhibitions - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_congress", methods=["POST", "GET"])
def edit_congress():
    if session.get('logged_in') and not session.get('submitted'):
        form = congress_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.office.data = select_show_record(session['code'], session['subject'])[0][9]
        form.contact_num.data = select_show_record(session['code'], session['subject'])[0][10]
        form.contact_pos.data = select_show_record(session['code'], session['subject'])[0][11]
        form.country.data = select_show_record(session['code'], session['subject'])[0][12]
        form.city.data = select_show_record(session['code'], session['subject'])[0][13]
        form.salon.data = select_show_record(session['code'], session['subject'])[0][14]
        form.frame.data = select_show_record(session['code'], session['subject'])[0][15]
        form.meh_moh.data = select_show_record(session['code'], session['subject'])[0][16]
        form.famous_persons.data = select_show_record(session['code'], session['subject'])[0][17]
        form.sokhanrans.data = select_show_record(session['code'], session['subject'])[0][18]

        if request.method == "POST":
            congress_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                            request.form["office"], request.form["contact_num"],
                            request.form["contact_pos"], request.form["country"], request.form["city"],
                            request.form["salon"], request.form["frame"], request.form["meh_moh"],
                            request.form["famous_persons"], request.form["sokhanrans"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("congress - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_bought_photos", methods=["POST", "GET"])
def edit_bought_photos():
    if session.get('logged_in') and not session.get('submitted'):
        form = bought_photos_form()
        form.photo_subject.data = select_show_record(session['code'], session['subject'])[0][8]
        form.number.data = select_show_record(session['code'], session['subject'])[0][9]
        form.tar_ghar.data = select_show_record(session['code'], session['subject'])[0][10]

        if request.method == "POST":
            bought_photos_record(1, select_first_record(session['code'], session['subject']),
                                 request.form["photo_subject"], request.form["number"],
                                 request.form["tar_ghar"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("bought_photos - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_letters_expert", methods=["POST", "GET"])
def edit_letters_expert():
    if session.get('logged_in') and not session.get('submitted'):
        form = bachelor_written()
        form.kar_number.data = select_show_record(session['code'], session['subject'])[0][8]
        form.accepted_number.data = select_show_record(session['code'], session['subject'])[0][9]
        form.frame.data = select_show_record(session['code'], session['subject'])[0][10]

        if request.method == "POST":
            letters_expert_record(1, select_first_record(session['code'], session['subject']),
                                  request.form["kar_number"], request.form["accepted_number"],
                                  request.form["frame"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("letters_expert - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_festivals_detailed", methods=["POST", "GET"])
def edit_festivals_detailed():
    if session.get('logged_in') and not session.get('submitted'):
        form = festivals_detailed_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.subject.data = select_show_record(session['code'], session['subject'])[0][9]
        form.art_dab.data = select_show_record(session['code'], session['subject'])[0][10]
        form.all_asar.data = select_show_record(session['code'], session['subject'])[0][11]
        form.take_parted_person.data = select_show_record(session['code'], session['subject'])[0][12]
        form.os_city.data = select_show_record(session['code'], session['subject'])[0][13]
        form.city.data = select_show_record(session['code'], session['subject'])[0][14]
        form.finished_asar.data = select_show_record(session['code'], session['subject'])[0][15]
        form.salon.data = select_show_record(session['code'], session['subject'])[0][16]
        form.choosing_asar_team.data = select_show_record(session['code'], session['subject'])[0][17]
        form.referees.data = select_show_record(session['code'], session['subject'])[0][18]
        form.asar_parted_num.data = select_show_record(session['code'], session['subject'])[0][19]
        form.international_rec.data = select_show_record(session['code'], session['subject'])[0][20]
        form.area_rec.data = select_show_record(session['code'], session['subject'])[0][21]
        form.asar_parted_in_dif.data = select_show_record(session['code'], session['subject'])[0][22]
        form.women.data = select_show_record(session['code'], session['subject'])[0][23]
        form.men.data = select_show_record(session['code'], session['subject'])[0][24]

        if request.method == "POST":
            festivals_detailed_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                                      request.form["subject"], request.form["art_dab"],
                                      request.form["all_asar"], request.form["take_parted_person"],
                                      request.form["os_city"],
                                      request.form["city"], request.form["finished_asar"], request.form["salon"],
                                      request.form["choosing_asar_team"],
                                      request.form["referees"], request.form["asar_parted_num"],
                                      request.form["international_rec"],
                                      request.form["area_rec"], request.form["asar_parted_in_dif"], request.form["women"],
                                      request.form["men"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("festivals_detailed - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_letters", methods=["POST", "GET"])
def edit_letters():
    if session.get('logged_in') and not session.get('submitted'):
        form = letters_form()
        # print select_first_record(session['code'], session['subject'])
        if request.method == "POST":
            session['subject'] = request.form["result_kind"]
            if form.result_kind.data == 'کتاب':
                return redirect(url_for('book'))
            else:
                return redirect(url_for('journal'))

        return render_template("letters - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_book", methods=["POST", "GET"])
def edit_book():
    if session.get('logged_in') and not session.get('submitted'):
        form = book_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.author.data = select_show_record(session['code'], session['subject'])[0][9]
        form.translator.data = select_show_record(session['code'], session['subject'])[0][10]
        form.nasher.data = select_show_record(session['code'], session['subject'])[0][11]
        form.lang.data = select_show_record(session['code'], session['subject'])[0][12]
        form.print_turn.data = select_show_record(session['code'], session['subject'])[0][13]
        form.sub_frame.data = select_show_record(session['code'], session['subject'])[0][14]
        form.roo_bar.data = select_show_record(session['code'], session['subject'])[0][15]
        form.nasher_city.data = select_show_record(session['code'], session['subject'])[0][16]
        form.meh_moh.data = select_show_record(session['code'], session['subject'])[0][17]
        form.shomargan_num.data = select_show_record(session['code'], session['subject'])[0][18]
        form.pages.data = select_show_record(session['code'], session['subject'])[0][19]

        if request.method == "POST":
            book_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                        request.form["author"], request.form["translator"],
                        request.form["nasher"], request.form["lang"], request.form["print_turn"],
                        request.form["sub_frame"], request.form["roo_bar"], request.form["nasher_city"],
                        request.form["meh_moh"], request.form["shomargan_num"], request.form["pages"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("book - edit.html", form=form, this_page=session['user'], main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


@app.route("/edit_journal", methods=["POST", "GET"])
def edit_journal():
    if session.get('logged_in') and not session.get('submitted'):
        form = journal_form()
        form.name.data = select_show_record(session['code'], session['subject'])[0][8]
        form.head_name.data = select_show_record(session['code'], session['subject'])[0][9]
        form.print_turn.data = select_show_record(session['code'], session['subject'])[0][10]
        form.shomargan_num.data = select_show_record(session['code'], session['subject'])[0][11]
        form.pages.data = select_show_record(session['code'], session['subject'])[0][12]
        form.frame.data = select_show_record(session['code'], session['subject'])[0][13]
        form.roo_bar.data = select_show_record(session['code'], session['subject'])[0][14]
        form.nasher_city.data = select_show_record(session['code'], session['subject'])[0][15]
        form.festival_name.data = select_show_record(session['code'], session['subject'])[0][16]
        form.meh_moh.data = select_show_record(session['code'], session['subject'])[0][17]

        if request.method == "POST":
            journal_record(1, select_first_record(session['code'], session['subject']), request.form["name"],
                           request.form["head_name"], request.form["print_turn"],
                           request.form["shomargan_num"], request.form["pages"], request.form["frame"],
                           request.form["roo_bar"], request.form["nasher_city"],
                           request.form["festival_name"], request.form["meh_moh"])
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('edit_record'))

        return render_template("journal - edit.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('edit_record'))


if __name__ == "__main__":
    app.run(debug=True)
