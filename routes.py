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
                    return redirect(url_for('add_record'))
                else:
                    error = "رمز عبور اشتباه است"
        return render_template("index.html", form=form, error=error)
    return redirect(url_for('add_record'))


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
                # return "validated"
                session['subject'] = form.subject.data
                if form.subject.data != 'مکتوبات':
                    if auth_code(form.code.data, form.subject.data):
                        error = 'این کد قبلا ثبت شده است'
                    else:
                        session['first_records'] = {'code': form.code.data, 'manager_name': form.manager_name.data,
                                                    'm_s_e': form.m_s_e.data, 'm_t_e': form.m_t_e.data,
                                                    'm_p_k': form.m_p_k.data,
                                                    'rec_date_day': form.rec_date_day.data,
                                                    'rec_date_month': form.rec_date_month.data,
                                                    'rec_date_year': form.rec_date_year.data,
                                                    'subject': form.subject.data}

                        for i in range(page_dict.keys().__len__()):
                            if page_dict.keys()[i] == form.subject.data and form.subject.data != 'مکتوبات':
                                return redirect(url_for(page_dict.values()[i]))
                elif form.subject.data == 'مکتوبات':
                    return redirect(url_for('letters'))

        if session.get('added'):
            message = 'گزارش با موفقیت ثبت شد'
            session['added'] = 0
        return render_template("add_record.html", this_page=session['user'], form=form, error=error, message=message)
    return redirect('index')


@app.route("/show", methods=["POST", "GET"])
def show():
    if session.get('logged_in') and not session['submitted']:
        form = show_form()
        if request.method == "POST":
            show_record(session['first_records'], form.name.data, form.author.data, form.director.data,
                        form.place.data, form.salon.data, form.frame.data,
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
            studio_record(session['first_records'], form.group_name.data, form.col_name.data, form.group_head.data,
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
            projects_record(session['first_records'], form.name.data, form.proj_res_name.data, form.gerd_vaz.data,
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
            photography_projects_record(session['first_records'], form.name.data, form.photo_subject.data,
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
            festivals_record(session['first_records'], form.name.data, form.fest_subjects.data, form.level.data,
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
            romance_record(session['first_records'], form.sent_asar_num.data, form.seen_asar_num.data,
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
            sessions_record(session['first_records'], form.name.data, form.session_subject.data, form.prof_name.data,
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
            multimedia_record(session['first_records'], form.name.data, form.frame.data, form.center.data,
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
            enghelab_lib_record(session['first_records'], form.ex_subjects_number.data, form.ex_resource_number.data,
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
            jang_lib_record(session['first_records'], form.ex_subjects_number.data, form.ex_resource_number.data,
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
            results_review_record(session['first_records'], form.kar_num.data, form.accepted_num.data,
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
            poem_expert_record(session['first_records'], form.sent_asar.data, form.seen_asar_num.data,
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
            plato_record(session['first_records'], form.group_name.data, form.director.data, form.name.data,
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
            visual_products_record(session['first_records'], form.major_name.data, form.number.data,
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
            music_products_record(session['first_records'], form.music_name.data, form.outing_pos.data,
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
            research_record(session['first_records'], form.research_name.data, form.author.data,
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
            exhibitions_record(session['first_records'], form.name.data, form.show_subject.data, form.os_city.data,
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
            congress_record(session['first_records'], form.name.data, form.office.data, form.contact_num.data,
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
            bought_photos_record(session['first_records'], form.photo_subject.data, form.number.data,
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
            letters_expert_record(session['first_records'], form.kar_number.data, form.accepted_number.data,
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
            festivals_detailed_record(session['first_records'], form.name.data, form.subject.data, form.art_dab.data,
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
                return redirect(url_for('book'))
            else:
                return redirect(url_for('journal'))

        return render_template("letters.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


@app.route("/book", methods=["POST", "GET"])
def book():
    if session.get('logged_in') and not session.get('submitted'):
        form = book_form()
        if request.method == "POST":
            book_record(session['first_records'], form.name.data, form.author.data, form.translator.data,
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
            journal_record(session['first_records'], form.name.data, form.head_name.data, form.print_turn.data,
                           form.shomargan_num.data, form.pages.data, form.frame.data,
                           form.roo_bar.data, form.nasher_city.data, form.festival_name.data, form.meh_moh.data)
            session['added'] = 1
            session['submitted'] = 1
            return redirect(url_for('add_record'))

        return render_template("journal.html", form=form, this_page=session['user'],
                               main_subject=session.get('subject'))
    return redirect(url_for('add_record'))


if __name__ == "__main__":
    app.run(debug=True)
