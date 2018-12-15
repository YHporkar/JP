# -*- coding: utf-8 -*-

import sqlite3
# from flask.ext.sqlalchemy import SQLAlchemy
# from werkzeug import generate_password_hash, check_password_hash

import geocoder
import urllib2
import json

page_dict = {'نمایش': 'show', 'استودیو': 'studio', 'پروژه_ها': 'projects',
             'پروژه_های_عکاسی': 'photography_projects', 'جشنواره_ها': 'festivals', 'کارشناسی_رمان': 'romance',
             'جلسات_و_کارگاه_ها': 'sessions', 'چند_رسانه_ای': 'multimedia', 'کتابخانه_انقلاب': 'enghelab_lib',
             'کتابخانه_جنگ': 'jang_lib', 'بازبینی_آثار': 'results_review', 'کارشناسی_شعر': 'poem_expert',
             'کارکرد_پلاتوها': 'plato', 'محصولات_تجسمی': 'visual_products', 'محصولات_موسیقی': 'music_products',
             'پژوهش': 'research', 'نمایشگاه_ها': 'exhibitions', 'همایش_ها': 'congress',
             'عکس_های_خریداری_شده': 'bought_photos', 'کارشناسی_آثار_مکتوب': 'letters_expert',
             'جشنواره_ها_تفصیلی': 'festivals_detailed', 'کتاب': 'book', 'نشریه': 'journal'}

db_name = "Records_DB"


def make_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS  Admin (
                      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                      username VARCHAR(200) NOT NULL ,
                      password VARCHAR(200) NOT NULL ,
                      is_online INTEGER NOT NULL DEFAULT 0);
                      ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS نمایش (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      author VARCHAR(200),
                      director VARCHAR(200),
                      show_place VARCHAR(200),
                      show_salon VARCHAR(200),
                      show_kind VARCHAR(200),
                      show_frame VARCHAR(200),
                      show_num VARCHAR(200),
                      contacts_num INTEGER,
                      contacts_pos VARCHAR(200),
                      meh_moh VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS استودیو (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      group_name VARCHAR(200),
                      col_name VARCHAR(200),
                      group_head VARCHAR(200),
                      mah_fa VARCHAR(200),
                      using_time INTEGER,
                      famous_person VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                  ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS پروژه_ها (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      proj_res_name VARCHAR(200),
                      gerd_vaz INTEGER,
                      ach_vaz INTEGER,
                      pey_office VARCHAR(200),
                      subject_description VARCHAR(1000),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''
                      CREATE TABLE IF NOT EXISTS پروژه_های_عکاسی (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      photo_subject VARCHAR(200),
                      photographer_name VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS جشنواره_ها (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      fest_subjects VARCHAR(200),
                      level VARCHAR(200),
                      country VARCHAR(200),
                      city VARCHAR(200),
                      salon VARCHAR(200),
                      referee VARCHAR(200),
                      amalkard_description VARCHAR(1000),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS کارشناسی_رمان (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      sent_asar_num INTEGER,
                      seen_asar_num INTEGER,
                      short_story_num INTEGER,
                      romance_num INTEGER,
                      sent_to_mehr_asar_num INTEGER,
                      sent_to_city_asar_num INTEGER,
                      printed_num INTEGER,
                      in_printed_num INTEGER,
                      rejected_num INTEGER,
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                  ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS جلسات_و_کارگاه_ها (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      session_subject VARCHAR(200),
                      prof_name VARCHAR(200),
                      contacts_num INTEGER,
                      count INTEGER,
                      country VARCHAR(200),
                      city VARCHAR(200),
                      salon VARCHAR(200),
                      level VARCHAR(200),
                      office VARCHAR(200),
                      achievements VARCHAR(200),
                      meh_moh1 VARCHAR(200),
                      meh_moh2 VARCHAR(200),
                      meh_moh3 VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS چند_رسانه_ای (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      frame VARCHAR(200),
                      center VARCHAR(200),
                      used_place VARCHAR(200),
                      producted_place VARCHAR(200),
                      product_time VARCHAR(200),
                      used VARCHAR(200),
                      meh_moh VARCHAR(200),
                      description VARCHAR(1000),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                  ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS بازبینی_آثار (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      kar_num INTEGER,
                      accepted_num INTEGER,
                      show_kind VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS کارشناسی_شعر (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      sent_asar INTEGER,
                      seen_asar_num INTEGER,
                      one_asar_num INTEGER,
                      collections_num INTEGER,
                      sent_to_mehr_asar_num INTEGER,
                      sent_to_city_asar_num INTEGER,
                      printed_num INTEGER,
                      in_printed_num INTEGER,
                      rejected_num INTEGER,
                      famous_persons VARCHAR(500),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS کارکرد_پلاتوها (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      group_name VARCHAR(200),
                      director VARCHAR(200),
                      name VARCHAR(200),
                      clock_num INTEGER,
                      program_kind VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS محصولات_تجسمی (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      major_name VARCHAR(200),
                      number INTEGER,
                      producers_name VARCHAR(500),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS محصولات_موسیقی (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      music_name VARCHAR(200),
                      outing_pos VARCHAR(200),
                      outing_turn VARCHAR(200),
                      frame VARCHAR(200),
                      music_kind VARCHAR(200),
                      singer VARCHAR(200),
                      music_producer VARCHAR(200),
                      tirax INTEGER,
                      meh_moh VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS پژوهش (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      research_name VARCHAR(200),
                      author VARCHAR(200),
                      research_subject VARCHAR(200),
                      outing_place VARCHAR(200),
                      meh_moh VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS نمایشگاه_ها (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      show_subject VARCHAR(200),
                      os_city VARCHAR(200),
                      city VARCHAR(200),
                      contacts_num INTEGER,
                      meh_moh VARCHAR(200),
                      finish_date DATE,
                      description VARCHAR(1000),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS همایش_ها (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      office VARCHAR(200),
                      contacts_num INTEGER,
                      contact_pos VARCHAR(200),
                      country VARCHAR(200),
                      city VARCHAR(200),
                      salon VARCHAR(200),
                      frame VARCHAR(200),
                      meh_moh VARCHAR(200),
                      famous_persons VARCHAR(500),
                      sokhanrans VARCHAR(400),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS عکس_های_خریداری_شده(
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      photo_subject VARCHAR(200),
                      number INTEGER,
                      tar_ghar VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS کارشناسی_آثار_مکتوب (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      kar_number INTEGER,
                      accepted_number INTEGER,
                      research VARCHAR(200),
                      namayesh_name VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS جشنواره_ها_تفصیلی (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      subject VARCHAR(200),
                      art_dab VARCHAR(200),
                      all_asar INTEGER,
                      take_parted_person INTEGER,
                      os_city VARCHAR(200),
                      city VARCHAR(200),
                      finished_asar INTEGER,
                      salon VARCHAR(200),
                      choosing_asar_team VARCHAR(200),
                      referees VARCHAR(200),
                      asar_parted_num VARCHAR(1000),
                      international_rec VARCHAR(1000),
                      area_rec VARCHAR(1000),
                      asar_parted_in_dif VARCHAR(1000),
                      women INTEGER,
                      men INTEGER,
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS کتاب (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      author VARCHAR(200),
                      translator VARCHAR(200),
                      nasher VARCHAR(200),
                      lang VARCHAR(200),
                      print_turn INTEGER,
                      sub_frame VARCHAR(200),
                      roo_bar INTEGER,
                      nasher_city VARCHAR(200),
                      meh_moh VARCHAR(200),
                      shomargan_num INTEGER,
                      pages INTEGER,
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS نشریه (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      name VARCHAR(200),
                      head_name VARCHAR(200),
                      print_turn INTEGER,
                      shomargan_num INTEGER,
                      pages INTEGER,
                      frame VARCHAR(200),
                      roo_bar INTEGER,
                      nasher_city VARCHAR(200),
                      festival_name VARCHAR(200),
                      meh_moh VARCHAR(200),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS کتابخانه_انقلاب (
                      id VARCHAR(200) PRIMARY KEY NOT NULL ,
                      manager VARCHAR(200),
                      m_p_k VARCHAR(200),
                      m_s_e VARCHAR(200),
                      m_t_e VARCHAR(200),
                      rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                      ex_subjects_number INTEGER,
                      ex_resource_number INTEGER,
                      ex_digital_resource_number INTEGER,
                      ex_pn_resource_number INTEGER,
                      lang1 VARCHAR(200),
                      lang2 VARCHAR(200),
                      lang3 VARCHAR(200),
                      new_subjects_number INTEGER,
                      new_resource_number INTEGER,
                      new_digital_resource_number INTEGER,
                      new_pn_resource_number INTEGER,
                      couns_pn_number INTEGER,
                      couns_research_proj_number INTEGER,
                      pn_subjects_number INTEGER,
                      lib_members_number INTEGER,
                      lib_members_number_thisYear INTEGER,
                      lib_members_women INTEGER,
                      lib_members_men INTEGER,
                      lib_members_diplom INTEGER,
                      lib_members_kardani INTEGER,
                      lib_members_karshenasi INTEGER,
                      lib_members_doctori INTEGER,
                      borrowed_book_number INTEGER,
                      borrowed_nash_number INTEGER,
                      borrowed_digital_number INTEGER,
                      borrowed_pn_number INTEGER,
                      description VARCHAR(1000),
                      valued INTEGER NOT NULL DEFAULT 0
                      );
                      ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS کتابخانه_جنگ (
                          id VARCHAR(200) PRIMARY KEY NOT NULL ,
                          manager VARCHAR(200),
                          m_p_k VARCHAR(200),
                          m_s_e VARCHAR(200),
                          m_t_e VARCHAR(200),
                          rec_date_year INTEGER, rec_date_month INTEGER, rec_date_day INTEGER,
                          ex_subjects_number INTEGER,
                          ex_resource_number INTEGER,
                          ex_digital_resource_number INTEGER,
                          ex_pn_resource_number INTEGER,
                          lang1 VARCHAR(200),
                          lang2 VARCHAR(200),
                          lang3 VARCHAR(200),
                          new_subjects_number INTEGER,
                          new_resource_number INTEGER,
                          new_digital_resource_number INTEGER,
                          new_pn_resource_number INTEGER,
                          couns_pn_number INTEGER,
                          couns_research_proj_number INTEGER,
                          pn_subjects_number INTEGER,
                          lib_members_number INTEGER,
                          lib_members_number_thisYear INTEGER,
                          lib_members_women INTEGER,
                          lib_members_men INTEGER,
                          lib_members_diplom INTEGER,
                          lib_members_kardani INTEGER,
                          lib_members_karshenasi INTEGER,
                          lib_members_doctori INTEGER,
                          borrowed_book_number INTEGER,
                          borrowed_nash_number INTEGER,
                          borrowed_digital_number INTEGER,
                          borrowed_pn_number INTEGER,
                          description VARCHAR(1000),
                          valued INTEGER NOT NULL DEFAULT 0
                          );
                          ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ارزیابی (
                        time_management VARCHAR(200), 
                        people_cooperation VARCHAR(200), 
                        hold_displn VARCHAR(200), 
                        advertising VARCHAR(200), 
                        sharee_time VARCHAR(200), 
                        decor_tansb VARCHAR(200), 
                        sound_quality VARCHAR(200), 
                        light_quality VARCHAR(200), 
                        area_adv VARCHAR(200), 
                        attr_audience VARCHAR(200), 
                        famous_persons VARCHAR(200), 
                        power_points_imp VARCHAR(200), 
                        tah_able_imp VARCHAR(200), 
                        description VARCHAR(200), 
                        trip_summerize VARCHAR(200), 
                        evaluator_name VARCHAR(200)
                      );                  
                      ''')
    conn.close()


def change_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    subject = page_dict.keys()
    for sub in subject:
        cursor.execute('''
                          ALTER TABLE %s ADD COLUMN contract VARCHAR(200);
                      ''' % sub)

        cursor.execute('''
                              ALTER TABLE %s ADD COLUMN performance VARCHAR(200);
                       ''' % sub)

        cursor.execute('''
                              ALTER TABLE %s ADD COLUMN strategic VARCHAR(200);
                       ''' % sub)

    conn.commit()
    conn.close()


# change_db(db_name)


def authenticate_Admin(username, password):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("select * from Admin where \
                    username='%s' and password='%s';" % (username, password))

    users = cursor.fetchall()
    return len(users) == 1


def make_hashed_password(password):
    import hashlib
    salt = "Salavat_bar_mohammad"
    hash = hashlib.sha1(salt + password).hexdigest()
    return hash


def new_Admin(username, password):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("insert into \
    Admin (username, password) \
    VALUES ('%s','%s','%s')" % (username, make_hashed_password(password)))

    conn.commit()
    conn.close()


def is_online(username):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT is_online FROM Admin WHERE username = '%s';" % username)
    online = cursor.fetchall()[0][0]

    if online:
        return True
    return False


def make_online(username):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE Admin SET is_online = 1 WHERE username = '%s';" % username)

    conn.commit()
    conn.close()


def make_offline(username):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE Admin SET is_online = 0 WHERE username = '%s';" % username)

    conn.commit()
    conn.close()


def auth_code(code, subject):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM %s WHERE id = '%s';" % (subject, code))

    rec = cursor.fetchall()
    conn.close()
    return len(rec) == 1


def evaluated_num_cal(subjects):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    i = 0
    for subject in subjects:
        cursor.execute("SELECT count(valued) FROM %s WHERE valued=0" % subject)
        i += cursor.fetchall()[0][0]
    return i


def evaluated(code, subject):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT valued FROM %s WHERE id = '%s';" % (subject, code))
    return cursor.fetchall()[0][0]


def first_record(first_records, edit_mode):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    if not edit_mode:
        cursor.execute("INSERT INTO %s (id, contract, manager, m_p_k, m_s_e, m_t_e, performance, strategic,"
                       " rec_date_year, rec_date_month, rec_date_day)"
                       " VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"
                       % (first_records['subject'], first_records['code'], first_records['contract'], first_records['manager_name'],
                          first_records['m_p_k'], first_records['m_s_e'], first_records['m_t_e'],
                          first_records['performance'], first_records['strategic'],
                          first_records['rec_date_year'], first_records['rec_date_month'],
                          first_records['rec_date_day']))
    elif edit_mode:
        cursor.execute("UPDATE %s SET manager = '%s', m_p_k = '%s'"
                       ", m_s_e = '%s', m_t_e = '%s', rec_date_year = '%s', rec_date_month = '%s',"
                       " rec_date_day = '%s' WHERE id= '%s';"
                       % (first_records['subject'], first_records['manager_name'],
                          first_records['m_p_k'], first_records['m_s_e'], first_records['m_t_e'],
                          first_records['rec_date_year'], first_records['rec_date_month'],
                          first_records['rec_date_day'], first_records['code']))
    conn.commit()
    conn.close()


def select_first_record(code, subject):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''SELECT id, manager, m_p_k, m_s_e, m_t_e, rec_date_year, rec_date_month, rec_date_day
                      FROM %s WHERE id = '%s';''' % (subject, code))
    rec = cursor.fetchall()
    return {'subject': subject, 'code': rec[0][0], 'manager_name': rec[0][1], 'm_p_k': rec[0][2], 'm_s_e': rec[0][3],
            'm_t_e': rec[0][4], 'rec_date_year': rec[0][5], 'rec_date_month': rec[0][6], 'rec_date_day': rec[0][7]}


def select_record(code, subject):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM %s WHERE id='%s';''' % (subject, code))

    return cursor.fetchall()


def select_rec_by_subject(subject):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM %s;''' % subject)
    rec = cursor.fetchall()
    return rec


def select_rec_by_subject_unit(subject, unit):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    unit_code = unit + '%'
    cursor.execute(''' SELECT * FROM %s WHERE id LIKE '%s';''' % (subject, unit_code))
    rec = cursor.fetchall()
    return rec


def select_rec_by_subject_eval(subject, valued):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM %s WHERE valued = '%s';''' % (subject, valued))
    rec = cursor.fetchall()
    return rec


def add_eval(time_management, people_cooperation, hold_displn, advertising, sharee_time, decor_tansb, sound_quality,
             light_quality, area_adv, attr_audience, famous_persons, power_points_imp, tah_able_imp, description,
             trip_summerize, evaluator_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ارزیابی"
                   " VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
                       time_management, people_cooperation, hold_displn, advertising, sharee_time, decor_tansb,
                       sound_quality,
                       light_quality, area_adv, attr_audience, famous_persons, power_points_imp, tah_able_imp,
                       description,
                       trip_summerize, evaluator_name))
    conn.commit()
    conn.close()


def show_record(edit_mode, first_records, name, author, director, show_place, show_salon, show_kind, show_frame,
                show_num, contacts_num,
                contacts_pos, meh_moh):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE نمایش SET name = '%s', author = '%s', director = '%s',"
                   " show_place = '%s', show_salon = '%s', show_kind = '%s', show_frame = '%s', show_num = '%s',"
                   " contacts_num = '%s', contacts_pos = '%s', meh_moh = '%s'"
                   "WHERE id = '%s';" % (
                       name, author, director, show_place, show_salon, show_kind, show_frame, show_num,
                       contacts_num, contacts_pos, meh_moh, first_records['code']))

    conn.commit()
    conn.close()


def studio_record(edit_mode, first_records, group_name, col_name, group_head, mah_fa, using_time, famous_person):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE استودیو SET group_name = '%s', col_name = '%s', group_head = '%s',"
                   "mah_fa = '%s', using_time = '%s', famous_person = '%s'"
                   "WHERE id = '%s';" % (group_name, col_name, group_head, mah_fa, using_time, famous_person,
                                         first_records['code']))

    conn.commit()
    conn.close()


def projects_record(edit_mode, first_records, name, proj_res_name, gerd_vaz, ach_vaz, pey_office, subject_description):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE پروژه_ها SET name = '%s', proj_res_name = '%s', gerd_vaz = '%s',"
                   " ach_vaz = '%s', pey_office = '%s', subject_description = '%s'"
                   "WHERE id = '%s';" % (
                       name, proj_res_name, gerd_vaz, ach_vaz, pey_office, subject_description, first_records['code']))

    conn.commit()
    conn.close()


def photography_projects_record(edit_mode, first_records, name, photo_subject, photographer_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE پروژه_های_عکاسی SET name = '%s', photo_subject = '%s', photographer_name = '%s'"
                   "WHERE id = '%s';" % (name, photo_subject, photographer_name, first_records['code']))

    conn.commit()
    conn.close()


def festivals_record(edit_mode, first_records, name, fest_subjects, level, country, city, salon, referee,
                     amalkard_description):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE جشنواره_ها SET name = '%s', fest_subjects = '%s', level = '%s',"
                   " country = '%s', city = '%s', salon = '%s', referee = '%s',"
                   " amalkard_description = '%s'"
                   "WHERE id = '%s';" % (name, fest_subjects, level, country, city, salon, referee,
                                         amalkard_description, first_records['code']))

    conn.commit()
    conn.close()


def romance_record(edit_mode, first_records, sent_asar_num, seen_asar_num, short_story_num, romance_num,
                   sent_to_mehr_asar_num,
                   sent_to_city_asar_num, printed_num, in_printed_num, rejected_num):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE کارشناسی_رمان SET sent_asar_num = '%s', seen_asar_num = '%s', short_story_num = '%s',"
                   "romance_num = '%s', sent_to_mehr_asar_num = '%s', sent_to_city_asar_num = '%s', printed_num = '%s',"
                   "in_printed_num = '%s', rejected_num = '%s'"
                   "WHERE id = '%s';" % (sent_asar_num, seen_asar_num, short_story_num, romance_num,
                                         sent_to_mehr_asar_num, sent_to_city_asar_num, printed_num,
                                         in_printed_num, rejected_num, first_records['code']))

    conn.commit()
    conn.close()


def sessions_record(edit_mode, first_records, name, session_subject, prof_name, contacts_num, count, country, city,
                    salon, level, office, achievements, meh_moh1, meh_moh2, meh_moh3):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute('''UPDATE جلسات_و_کارگاه_ها SET name = '%s', session_subject = '%s', prof_name = '%s',
                   contacts_num = '%s', count = '%s', country = '%s', city = '%s',
                   salon = '%s', level = '%s', office = '%s', achievements = '%s', meh_moh1 = '%s',
                   meh_moh2 = '%s', meh_moh3 = '%s' WHERE id = '%s';'''
                   % (name, session_subject, prof_name, contacts_num, count, country, city,
                      salon, level, office, achievements, meh_moh1, meh_moh2, meh_moh3, first_records['code']))

    conn.commit()
    conn.close()


def multimedia_record(edit_mode, first_records, name, frame, center, used_place, producted_place, product_time, used,
                      meh_moh, description):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE چند_رسانه_ای SET name = '%s', frame = '%s', center = '%s',"
                   " used_place = '%s', producted_place = '%s', product_time = '%s', used = '%s',"
                   " meh_moh = '%s', description = '%s'"
                   "WHERE id = '%s';" % (name, frame, center, used_place, producted_place, product_time, used,
                                         meh_moh, description, first_records['code']))

    conn.commit()
    conn.close()


def enghelab_lib_record(edit_mode, first_records, ex_subjects_number, ex_resource_number,
                        ex_digital_resource_number, ex_pn_resource_number,
                        lang1, lang2, lang3, new_subjects_number,
                        new_resource_number, new_digital_resource_number,
                        new_pn_resource_number, couns_pn_number,
                        couns_research_proj_number, pn_subjects_number,
                        lib_members_number, lib_members_number_thisYear,
                        lib_members_women, lib_members_men,
                        lib_members_diplom, lib_members_kardani,
                        lib_members_karshenasi, lib_members_doctori,
                        borrowed_book_number, borrowed_nash_number,
                        borrowed_digital_number, borrowed_pn_number,
                        description):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute('''UPDATE کتابخانه_انقلاب SET ex_subjects_number = '%s', ex_resource_number = '%s', ex_digital_resource_number = '%s',
                   ex_pn_resource_number = '%s', lang1 = '%s', lang2 = '%s', lang3 = '%s', new_subjects_number = '%s',
                   new_resource_number = '%s', new_digital_resource_number = '%s', new_pn_resource_number = '%s',
                   couns_pn_number = '%s', couns_research_proj_number = '%s',
                   pn_subjects_number = '%s', lib_members_number = '%s', lib_members_number_thisYear = '%s',
                   lib_members_women = '%s', lib_members_men = '%s', lib_members_diplom = '%s',
                   lib_members_kardani = '%s', lib_members_karshenasi = '%s', lib_members_doctori = '%s',
                   borrowed_book_number = '%s', borrowed_nash_number = '%s', borrowed_digital_number = '%s',
                   borrowed_pn_number = '%s', description = '%s'
                   WHERE id = '%s';''' % (ex_subjects_number, ex_resource_number,
                                          ex_digital_resource_number, ex_pn_resource_number,
                                          lang1, lang2, lang3, new_subjects_number,
                                          new_resource_number, new_digital_resource_number,
                                          new_pn_resource_number, couns_pn_number,
                                          couns_research_proj_number, pn_subjects_number,
                                          lib_members_number, lib_members_number_thisYear,
                                          lib_members_women, lib_members_men,
                                          lib_members_diplom, lib_members_kardani,
                                          lib_members_karshenasi, lib_members_doctori,
                                          borrowed_book_number, borrowed_nash_number,
                                          borrowed_digital_number, borrowed_pn_number,
                                          description, first_records['code']))

    conn.commit()
    conn.close()


def jang_lib_record(edit_mode, first_records, ex_subjects_number, ex_resource_number,
                    ex_digital_resource_number, ex_pn_resource_number,
                    lang1, lang2, lang3, new_subjects_number,
                    new_resource_number, new_digital_resource_number,
                    new_pn_resource_number, couns_pn_number,
                    couns_research_proj_number, pn_subjects_number,
                    lib_members_number, lib_members_number_thisYear,
                    lib_members_women, lib_members_men,
                    lib_members_diplom, lib_members_kardani,
                    lib_members_karshenasi, lib_members_doctori,
                    borrowed_book_number, borrowed_nash_number,
                    borrowed_digital_number, borrowed_pn_number,
                    description):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute('''UPDATE کتابخانه_جنگ SET ex_subjects_number = '%s', ex_resource_number = '%s', ex_digital_resource_number = '%s',
                   ex_pn_resource_number = '%s', lang1 = '%s', lang2 = '%s', lang3 = '%s', new_subjects_number = '%s',
                   new_resource_number = '%s', new_digital_resource_number = '%s', new_pn_resource_number = '%s',
                   couns_pn_number = '%s', couns_research_proj_number = '%s',
                   pn_subjects_number = '%s', lib_members_number = '%s', lib_members_number_thisYear = '%s',
                   lib_members_women = '%s', lib_members_men = '%s', lib_members_diplom = '%s',
                   lib_members_kardani = '%s', lib_members_karshenasi = '%s', lib_members_doctori = '%s',
                   borrowed_book_number = '%s', borrowed_nash_number = '%s', borrowed_digital_number = '%s',
                   borrowed_pn_number = '%s', description = '%s'
                   WHERE id = '%s';''' % (ex_subjects_number, ex_resource_number,
                                          ex_digital_resource_number, ex_pn_resource_number,
                                          lang1, lang2, lang3, new_subjects_number,
                                          new_resource_number, new_digital_resource_number,
                                          new_pn_resource_number, couns_pn_number,
                                          couns_research_proj_number, pn_subjects_number,
                                          lib_members_number, lib_members_number_thisYear,
                                          lib_members_women, lib_members_men,
                                          lib_members_diplom, lib_members_kardani,
                                          lib_members_karshenasi, lib_members_doctori,
                                          borrowed_book_number, borrowed_nash_number,
                                          borrowed_digital_number, borrowed_pn_number,
                                          description, first_records['code']))

    conn.commit()
    conn.close()


def results_review_record(edit_mode, first_records, kar_num, accepted_num, show_kind):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE بازبینی_آثار SET kar_num = '%s', accepted_num = '%s', show_kind = '%s'"
                   "WHERE id = '%s';" % (kar_num, accepted_num, show_kind, first_records['code']))

    conn.commit()
    conn.close()


def poem_expert_record(edit_mode, first_records, sent_asar, seen_asar_num, collections_num,
                       one_asar_num, sent_to_mehr_asar_num, sent_to_city_asar_num,
                       printed_num, in_printed_num, rejected_num, famous_persons):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE کارشناسی_شعر SET sent_asar = '%s', seen_asar_num = '%s', collections_num = '%s',"
                   "one_asar_num = '%s', sent_to_mehr_asar_num = '%s', sent_to_city_asar_num = '%s',"
                   " printed_num = '%s',in_printed_num = '%s', rejected_num = '%s', famous_persons = '%s'"
                   "WHERE id = '%s';" % (sent_asar, seen_asar_num, collections_num,
                                         one_asar_num, sent_to_mehr_asar_num, sent_to_city_asar_num,
                                         printed_num, in_printed_num, rejected_num, famous_persons,
                                         first_records['code']))

    conn.commit()
    conn.close()


def plato_record(edit_mode, first_records, group_name, director, name, clock_num, program_kind):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE کارکرد_پلاتوها SET group_name = '%s', director = '%s', name = '%s',"
                   "clock_num = '%s', program_kind = '%s'"
                   "WHERE id = '%s';" % (group_name, director, name, clock_num, program_kind, first_records['code']))

    conn.commit()
    conn.close()


def visual_products_record(edit_mode, first_records, major_name, number, producers_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE محصولات_تجسمی SET major_name = '%s', number = '%s', producers_name = '%s'"
                   "WHERE id = '%s';" % (major_name, number, producers_name, first_records['code']))

    conn.commit()
    conn.close()


def music_products_record(edit_mode, first_records, music_name, outing_pos, outing_turn, frame, music_kind, singer,
                          music_producer, tirax, meh_moh):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE محصولات_موسیقی SET music_name = '%s', outing_pos = '%s', outing_turn = '%s',"
                   " frame = '%s', music_kind = '%s', singer = '%s', music_producer = '%s',"
                   " tirax = '%s', meh_moh = '%s'"
                   "WHERE id = '%s';" % (music_name, outing_pos, outing_turn, frame, music_kind, singer, music_producer,
                                         tirax, meh_moh, first_records['code']))

    conn.commit()
    conn.close()


def research_record(edit_mode, first_records, research_name, author, research_subject, outing_place, meh_moh):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE پژوهش SET research_name = '%s', author = '%s', research_subject = '%s',"
                   "outing_place = '%s', meh_moh = '%s'"
                   "WHERE id = '%s';" % (
                       research_name, author, research_subject, outing_place, meh_moh, first_records['code']))

    conn.commit()
    conn.close()


def exhibitions_record(edit_mode, first_records, name, show_subject, os_city,
                       city, contacts_num, meh_moh, finish_date_day, finish_date_month, finish_date_year, description):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE نمایشگاه_ها SET name = '%s', show_subject = '%s', os_city = '%s',"
                   " city = '%s', contacts_num = '%s', meh_moh = '%s', finish_date = '%s',"
                   " description = '%s'"
                   "WHERE id = '%s';" % (name, show_subject, os_city, city, contacts_num, meh_moh,
                                         (finish_date_day + '-' + finish_date_month + '-' + finish_date_year),
                                         description, first_records['code']))

    conn.commit()
    conn.close()


def congress_record(edit_mode, first_records, name, office, contacts_num,
                    contact_pos, country, city, salon, frame, meh_moh, famous_persons, sokhanrans):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE همایش_ها SET name = '%s', office = '%s', contacts_num = '%s',"
                   " contact_pos = '%s', country = '%s', city = '%s', salon = '%s',"
                   " frame = '%s', meh_moh = '%s', famous_persons = '%s', sokhanrans = '%s'"
                   "WHERE id = '%s';" % (name, office, contacts_num, contact_pos, country, city, salon,
                                         frame, meh_moh, famous_persons, sokhanrans, first_records['code']))

    conn.commit()
    conn.close()


def bought_photos_record(edit_mode, first_records, photo_subject, number, tar_ghar):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE عکس_های_خریداری_شده SET photo_subject = '%s', number = '%s', tar_ghar = '%s'"
                   "WHERE id = '%s';" % (photo_subject, number, tar_ghar, first_records['code']))

    conn.commit()
    conn.close()


def letters_expert_record(edit_mode, first_records, kar_number, accepted_number, research, namayesh_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE کارشناسی_آثار_مکتوب SET kar_number = '%s', accepted_number = '%s', research = '%s', namayesh_name = '%s'"
                   "WHERE id = '%s';" % (kar_number, accepted_number, research, namayesh_name, first_records['code']))

    conn.commit()
    conn.close()


def festivals_detailed_record(edit_mode, first_records, name, subject, art_dab,
                              all_asar, take_parted_person, os_city,
                              city, finished_asar, salon, choosing_asar_team,
                              referees, asar_parted_num, international_rec,
                              area_rec, asar_parted_in_dif, women,
                              men):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE جشنواره_ها_تفصیلی SET name = '%s', subject = '%s', art_dab = '%s',"
                   " all_asar = '%s', take_parted_person = '%s', os_city = '%s',city = '%s',"
                   "finished_asar = '%s', salon = '%s', choosing_asar_team = '%s', referees = '%s',"
                   " asar_parted_num = '%s', international_rec = '%s', area_rec = '%s',"
                   " asar_parted_in_dif = '%s', women = '%s', men = '%s'"
                   "WHERE id = '%s';" % (name, subject, art_dab, all_asar, take_parted_person, os_city, city,
                                         finished_asar, salon, choosing_asar_team, referees,
                                         asar_parted_num, international_rec, area_rec, asar_parted_in_dif,
                                         women, men, first_records['code']))

    conn.commit()
    conn.close()


def book_record(edit_mode, first_records, name, author, translator,
                nasher, lang, print_turn,
                sub_frame, roo_bar, nasher_city, meh_moh,
                shomargan_num, pages):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE کتاب SET name = '%s', author = '%s', translator = '%s',"
                   " nasher = '%s', lang = '%s', print_turn = '%s', sub_frame = '%s',"
                   " roo_bar = '%s', nasher_city = '%s', meh_moh = '%s', shomargan_num = '%s', pages = '%s'"
                   "WHERE id = '%s';" % (name, author, translator, nasher, lang, print_turn, sub_frame,
                                         roo_bar, nasher_city, meh_moh, shomargan_num, pages, first_records['code']))

    conn.commit()
    conn.close()


def journal_record(edit_mode, first_records, name, head_name, print_turn,
                   shomargan_num, pages, frame,
                   roo_bar, nasher_city, festival_name, meh_moh):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    first_record(first_records, edit_mode)
    cursor.execute("UPDATE نشریه SET name = '%s', head_name = '%s', print_turn = '%s',"
                   " shomargan_num = '%s', pages = '%s', frame = '%s', roo_bar = '%s',"
                   " nasher_city = '%s', festival_name = '%s', meh_moh = '%s'"
                   "WHERE id = '%s';" % (name, head_name, print_turn, shomargan_num, pages, frame, roo_bar,
                                         nasher_city, festival_name, meh_moh, first_records['code']))

    conn.commit()
    conn.close()


def search_record(first_records):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM %s WHERE id = '%s';" % (first_records['subject'], first_records['code']))

    rec = cursor.fetchall()
    conn.close()
    return len(rec) == 1


def set_evaluated(code, subject):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''UPDATE %s SET valued = 1 WHERE id = '%s';''' % (subject, code))
    conn.commit()
    conn.close()


def select_record_amar(unit, subject, year, from_month, to_month):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    unit_code = unit + '%'
    cursor.execute(''' SELECT * FROM %s WHERE rec_date_year='%s' and rec_date_month>='%s'
                       and rec_date_month<='%s' and id LIKE '%s';'''
                   % (subject, year, from_month, to_month, unit_code))

    return cursor.fetchall()


def select_contacts_num(unit, subject, year, from_month, to_month):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    unit_code = unit + '%'
    cursor.execute('''SELECT AVG(contacts_num) FROM %s WHERE id LIKE '%s' and rec_date_year='%s'
                      and rec_date_month>='%s' and rec_date_month<='%s';''' % (subject, unit_code, year, from_month, to_month))
    return cursor.fetchall()[0][0]


# select count of a subject's records according to their unit
def performance_percent(unit, subject, year, from_month, to_month):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    unit_code = unit + '%'
    cursor.execute('''SELECT COUNT(id) FROM %s WHERE id LIKE '%s' and rec_date_year='%s'
                      and rec_date_month>='%s' and rec_date_month<='%s';''' % (subject, unit_code, year, from_month, to_month))

    return cursor.fetchall()[0][0]


def select_by_month_year(unit, subject, month, year):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    unit_code = unit + '%'
    cursor.execute("SELECT COUNT(id) FROM %s WHERE id LIKE '%s' and rec_date_year='%s' and rec_date_month='%s';" %
                   (subject, unit_code, year, month))

    return cursor.fetchall()[0][0]


def insert():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    i = 2
    for unit in ['روابط عمومی', 'موسسه سپهر سوره مهر', 'مرکز آفرینش های ادبی', 'مرکز تجسمی',
                 'مرکز ترجمه', 'مرکز طنز', 'مرکز مطالعات و تحقیقات فرهنگ و ادب پایداری', 'مرکزک معماری',
                 'مرکز موسیقی', 'مرکز هنرهای نمایشی', 'کودک و نوجوان']:
        cursor.execute("INSERT INTO Admin (id, username, password) VALUES ('%s', '%s', '%s')" % (i, unit, 1))
        i += 1
    conn.commit()
    conn.close()

# insert()
make_database(db_name)
