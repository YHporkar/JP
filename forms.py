# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email, Length
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class Login(Form):
    username = SelectField('نام واحد',
                           choices=[('خانه عکاسان','خانه عکاسان'), ('روابط عمومی','روابط عمومی'), ('موسسه سپهر سوره مهر','موسسه سپهر سوره مهر'),
                                    ('مرکز آفرینش های ادبی','مرکز آفرینش های ادبی'), ('مرکز تجسمی','مرکز تجسمی'), ('مرکز ترجمه','مرکز ترجمه'),
                                    ('مرکز طنز','مرکز طنز'), ('مرکز مطالعات و تحقیقات فرهنگ و ادب پایداری', 'مرکز مطالعات و تحقیقات فرهنگ و ادب پایداری'),
                                    ('مرکز معماری', 'مرکز معماری'), ('مرکز موسیقی', 'مرکز موسیقی'), ('مرکز هنرهای نمایشی', 'مرکز هنرهای نمایشی'), ('کودک و نوجوان', 'کودک و نوجوان'),
                                    ('مرکز ارزیابی', 'مرکز ارزیابی')])
    password = PasswordField(validators=[DataRequired("لطفا رمز خود را وارد کنید")])
    login = SubmitField('ورود')


class adding_record(Form):
    code = StringField(validators=[DataRequired('لطفا کد را وارد کنید')])
    manager_name = StringField(validators=[DataRequired('لطفا نام مدیر را وارد کنید')])
    m_p_k = StringField(validators=[DataRequired('لطفا نام مسئول پیگیری کننده را وارد کنید')])
    m_s_e = StringField(validators=[DataRequired('لطفا کد را وارد کنید')])
    m_t_e = StringField(validators=[DataRequired('لطفا کد را وارد کنید')])
    rec_date_day = SelectField(choices=[(i, i) for i in range(1385, 1411)])
    rec_date_month = SelectField(choices=[(i, i) for i in range(1, 13)])
    rec_date_year = SelectField(choices=[(i, i) for i in range(1, 32)])
    subject = SelectField(choices=[('نمایش', 'نمایش'), ('استودیو', 'استودیو'), ('پروژه_ها', 'پروژه ها'),
                                   ('پروژه_های_عکاسی', 'پروژه های عکاسی'), ('جشنواره_ها', 'جشنواره ها'),
                                   ('کارشناسی_رمان', 'کارشناسی رمان'),
                                   ('جلسات_و_کارگاه_ها', 'جلسات و کارگاه ها'), ('چند_رسانه_ای', 'چند رسانه ای'),
                                   ('کتابخانه_انقلاب', 'کتابخانه انقلاب'),
                                   ('کتابخانه_جنگ', 'کتابخانه جنگ'), ('بازبینی_آثار', 'بازبینی آثار'),
                                   ('کارشناسی_شعر', 'کارشناسی شعر'),
                                   ('کارکرد_پلاتوها', 'کارکرد پلاتوها'), ('محصولات_تجسمی', 'محصولات تجسمی'),
                                   ('محصولات_موسیقی', 'محصولات موسیقی'),
                                   ('پژوهش', 'پژوهش'), ('نمایشگاه_ها', 'نمایشگاه ها'), ('همایش_ها', 'همایش ها'),
                                   ('عکس_های_خریداری_شده', 'عکس های خریداری شده'),
                                   ('کارشناسی_آثار_مکتوب', 'کارشناسی آثار مکتوب'),
                                   ('جشنواره_ها_تفصیلی', 'جشنواره ها-تفصیلی'), ('مکتوبات', 'مکتوبات')])
    continues = SubmitField('ادامه')
    search = SubmitField('جستجو')
    logout = SubmitField('خروج')


class records_first_info_form(Form):
    code = StringField()
    manager_name = StringField(render_kw={'readonly': True})
    m_p_k = StringField(render_kw={'readonly': True})
    m_s_e = StringField(render_kw={'readonly': True})
    m_t_e = StringField(render_kw={'readonly': True})
    rec_date_day = StringField(render_kw={'readonly': True})
    rec_date_month = StringField(render_kw={'readonly': True})
    rec_date_year = StringField(render_kw={'readonly': True})
    subject = StringField(render_kw={'readonly': True})
    back = SubmitField('بازگشت')
    continues = SubmitField('ادامه')
    logout = SubmitField('خروج')


class enter_evaluation(Form):
    code = StringField()
    name = StringField()
    time_management = SelectField()
    people_cooperation = SelectField()
    hold_displn = SelectField()
    advertising = SelectField()
    sharee_time = SelectField()
    decor_tansb = SelectField()
    sound_quality = SelectField()
    light_quality = SelectField()
    area_adv = SelectField()
    attr_audience = SelectField()
    famous_persons = SelectField()
    office = StringField()
    subject = StringField()
    power_points_imp = TextAreaField()
    tah_able_imp = TextAreaField()
    description = TextAreaField()
    trip_summerize = TextAreaField()
    evaluator_name = StringField()
    logout = SubmitField('خروج')

class editing_record(Form):
    code = StringField()
    manager_name = StringField()
    m_p_k = StringField()
    m_s_e = StringField()
    m_t_e = StringField()
    rec_date_day = SelectField(choices=[(i, i) for i in range(1385, 1411)])
    rec_date_month = SelectField(choices=[(i, i) for i in range(1, 13)])
    rec_date_year = SelectField(choices=[(i, i) for i in range(1, 32)])
    subject = SelectField(choices=[('نمایش', 'نمایش'), ('استودیو', 'استودیو'), ('پروژه_ها', 'پروژه ها'),
                                   ('پروژه_های_عکاسی', 'پروژه های عکاسی'), ('جشنواره_ها', 'جشنواره ها'),
                                   ('کارشناسی_رمان', 'کارشناسی رمان'),
                                   ('جلسات_و_کارگاه_ها', 'جلسات و کارگاه ها'), ('چند_رسانه_ای', 'چند رسانه ای'),
                                   ('کتابخانه_انقلاب', 'کتابخانه انقلاب'),
                                   ('کتابخانه_جنگ', 'کتابخانه جنگ'), ('بازبینی_آثار', 'بازبینی آثار'),
                                   ('کارشناسی_شعر', 'کارشناسی شعر'),
                                   ('کارکرد_پلاتوها', 'کارکرد پلاتوها'), ('محصولات_تجسمی', 'محصولات تجسمی'),
                                   ('محصولات_موسیقی', 'محصولات موسیقی'),
                                   ('پژوهش', 'پژوهش'), ('نمایشگاه_ها', 'نمایشگاه ها'), ('همایش_ها', 'همایش ها'),
                                   ('عکس_های_خریداری_شده', 'عکس های خریداری شده'),
                                   ('کارشناسی_آثار_مکتوب', 'کارشناسی آثار مکتوب'),
                                   ('جشنواره_ها_تفصیلی', 'جشنواره ها-تفصیلی'), ('مکتوبات', 'مکتوبات')])
    evaluated = SelectField(choices=[(1, 'ارزیابی شده'), (0, 'ارزیابی نشده')])
    search = SubmitField('جستجو')
    logout = SubmitField('خروج')


class show_form(Form):
    name = StringField(validators=[DataRequired()])
    author = StringField(validators=[DataRequired()])
    director = StringField(validators=[DataRequired()])
    place = StringField(validators=[DataRequired()])
    ejra_num = StringField(validators=[DataRequired()])
    contact_num = StringField(validators=[DataRequired()])
    contact_status = StringField(validators=[DataRequired()])
    salon = SelectField(choices=[('سالن اوستا', 'سالن اوستا'), ('سالن کنفرانس حوزه ریاست', 'سالن کنفرانس حوزه ریاست'), ('سالن ابوالفضل عالی', 'سالن ابوالفضل عالی'),
                                   ('سالن کنفرانس پژوهشگاه', 'سالن کنفرانس پژوهشگاه'), ('سالن سلمان هراتی', 'سالن سلمان هراتی'),
                                   ('تالار سوره', 'تالار سوره'),
                                   ('گالری شماره 2 خانه عکاسان ایران', 'گالری شماره 2 خانه عکاسان ایران'), ('سالن استاد امیرحسین فردی', 'سالن استاد امیرحسین فردی'),
                                   ('تالار اندیشه', 'تالار اندیشه'),
                                   ('تالار مهر', 'تالار مهر'), ('تالار ماه', 'تالار ماه'),
                                   ('محوطه حوزه هنری', 'محوطه حوزه هنری'),
                                   ('روبروی مسجد حضرت آیت الله خامنه ای', 'روبروی مسجد حضرت آیت الله خامنه ای'), ('گالری شماره 1 خانه عکاسان ایران', 'گالری شماره 1 خانه عکاسان ایران'),
                                   ('کارگاه مجسمه سازی', 'کارگاه مجسمه سازی'),
                                   ('مسجد حضرت آیت الله خامنه ای', 'مسجد حضرت آیت الله خامنه ای'), ('خانه عکاسان', 'خانه عکاسان'), ('مرکز آفرینش های ادبی', 'مرکز آفرینش های ادبی'),
                                   ('مرکز موسیقی', 'مرکز موسیقی'),
                                   ('مرکز پایداری', 'مرکز پایداری'),
                                   ('مرکز معماری', 'مرکز معماری'), ('مرکز طنز', 'مرکز طنز'), ('مرکز هنرهای نمایشی', 'مرکز هنرهای نمایشی')
                                    , ('مرکز روابط عمومی', 'مرکز روابط عمومی')])
    show_kind = SelectField(choices=[('بزرگسال', 'بزرگسال'), ('کودک و نوجوان', 'کودک و نوجوان')])
    frame = SelectField(choices=[('صحنه ای', 'صحنه ای'), ('خیابانی', 'خیابانی')])
    meh_moh = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')



class studio_form(Form):
    group_name = StringField(validators=[DataRequired()])
    col_name = StringField(validators=[DataRequired()])
    group_head = StringField(validators=[DataRequired()])
    mah_fa = SelectField(choices=[('داخلی', 'داخلی'), ('خارجی', 'خارجی')])
    using_time = StringField(validators=[DataRequired()])
    famous_person = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class projects_form(Form):
    name = StringField(validators=[DataRequired()])
    proj_res_name = StringField(validators=[DataRequired()])
    gerd_vaz = StringField(validators=[DataRequired()])
    ach_vaz = StringField(validators=[DataRequired()])
    pey_office = StringField(validators=[DataRequired()])
    subject_description = TextAreaField()
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class photography_projects_form(Form):
    name = StringField(validators=[DataRequired()])
    photo_subject = StringField(validators=[DataRequired()])
    photographer_name = StringField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class festivals_form(Form):
    name = StringField(validators=[DataRequired()])
    fest_subjects = StringField(validators=[DataRequired()])
    level = StringField(validators=[DataRequired()])
    country = StringField(validators=[DataRequired()])
    city = SelectField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'),
                                   ('اصفهان', 'اصفهان'), ('البرز', 'البرز'),
                                   ('ایلام', 'ایلام'),
                                   ('بوشهر', 'بوشهر'), ('تهران', 'تهران'),
                                   ('چهارمحال بختیاری', 'چهارمحال بختیاری'),
                                   ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'),
                                   ('خراسان شمالی', 'خراسان شمالی'),
                                   ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'),
                                   ('سمنان', 'سمنان'),
                                   ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'),
                                   ('قم', 'قم'),
                                   ('کردستان', 'کردستان'),
                                   ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهکیلویه و بویراحمد', 'کهکیلویه و بویراحمد'),
                                   ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'),
                                   ('مازندران', 'مازندران'),
                                   ('مرکزی', 'مرکزی'),
                                   ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'),
                                   ('یزد', 'یزد')])
    salon = SelectField(choices=[('سالن اوستا', 'سالن اوستا'), ('سالن کنفرانس حوزه ریاست', 'سالن کنفرانس حوزه ریاست'), ('سالن ابوالفضل عالی', 'سالن ابوالفضل عالی'),
                                   ('سالن کنفرانس پژوهشگاه', 'سالن کنفرانس پژوهشگاه'), ('سالن سلمان هراتی', 'سالن سلمان هراتی'),
                                   ('تالار سوره', 'تالار سوره'),
                                   ('گالری شماره 2 خانه عکاسان ایران', 'گالری شماره 2 خانه عکاسان ایران'), ('سالن استاد امیرحسین فردی', 'سالن استاد امیرحسین فردی'),
                                   ('تالار اندیشه', 'تالار اندیشه'),
                                   ('تالار مهر', 'تالار مهر'), ('تالار ماه', 'تالار ماه'),
                                   ('محوطه حوزه هنری', 'محوطه حوزه هنری'),
                                   ('روبروی مسجد حضرت آیت الله خامنه ای', 'روبروی مسجد حضرت آیت الله خامنه ای'), ('گالری شماره 1 خانه عکاسان ایران', 'گالری شماره 1 خانه عکاسان ایران'),
                                   ('کارگاه مجسمه سازی', 'کارگاه مجسمه سازی'),
                                   ('مسجد حضرت آیت الله خامنه ای', 'مسجد حضرت آیت الله خامنه ای'), ('خانه عکاسان', 'خانه عکاسان'), ('مرکز آفرینش های ادبی', 'مرکز آفرینش های ادبی'),
                                   ('مرکز موسیقی', 'مرکز موسیقی'),
                                   ('مرکز پایداری', 'مرکز پایداری'),
                                   ('مرکز معماری', 'مرکز معماری'), ('مرکز طنز', 'مرکز طنز'), ('مرکز هنرهای نمایشی', 'مرکز هنرهای نمایشی')
                                    , ('مرکز روابط عمومی', 'مرکز روابط عمومی')])
    referee = TextAreaField(validators=[DataRequired()])
    amalkard_description = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class bachelor_novel(Form):
    sent_asar_num = StringField(validators=[DataRequired()])
    seen_asar_num = StringField(validators=[DataRequired()])
    short_story_num = StringField(validators=[DataRequired()])
    romance_num = StringField(validators=[DataRequired()])
    sent_to_mehr_asar_num = StringField(validators=[DataRequired()])
    sent_to_city_asar_num = StringField(validators=[DataRequired()])
    printed_num = StringField(validators=[DataRequired()])
    in_printed_num = StringField(validators=[DataRequired()])
    rejected_num = StringField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class sessions_form(Form):
    name = StringField(validators=[DataRequired()])
    session_subject = StringField(validators=[DataRequired()])
    prof_name = StringField(validators=[DataRequired()])
    contact_avg = StringField(validators=[DataRequired()])
    count = StringField(validators=[DataRequired()])
    country = StringField(validators=[DataRequired()])
    city = SelectField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'),
                                   ('اصفهان', 'اصفهان'), ('البرز', 'البرز'),
                                   ('ایلام', 'ایلام'),
                                   ('بوشهر', 'بوشهر'), ('تهران', 'تهران'),
                                   ('چهارمحال بختیاری', 'چهارمحال بختیاری'),
                                   ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'),
                                   ('خراسان شمالی', 'خراسان شمالی'),
                                   ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'),
                                   ('سمنان', 'سمنان'),
                                   ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'),
                                   ('قم', 'قم'),
                                   ('کردستان', 'کردستان'),
                                   ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهکیلویه و بویراحمد', 'کهکیلویه و بویراحمد'),
                                   ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'),
                                   ('مازندران', 'مازندران'),
                                   ('مرکزی', 'مرکزی'),
                                   ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'),
                                   ('یزد', 'یزد')])
    salon = SelectField(choices=[('سالن اوستا', 'سالن اوستا'), ('سالن کنفرانس حوزه ریاست', 'سالن کنفرانس حوزه ریاست'), ('سالن ابوالفضل عالی', 'سالن ابوالفضل عالی'),
                                   ('سالن کنفرانس پژوهشگاه', 'سالن کنفرانس پژوهشگاه'), ('سالن سلمان هراتی', 'سالن سلمان هراتی'),
                                   ('تالار سوره', 'تالار سوره'),
                                   ('گالری شماره 2 خانه عکاسان ایران', 'گالری شماره 2 خانه عکاسان ایران'), ('سالن استاد امیرحسین فردی', 'سالن استاد امیرحسین فردی'),
                                   ('تالار اندیشه', 'تالار اندیشه'),
                                   ('تالار مهر', 'تالار مهر'), ('تالار ماه', 'تالار ماه'),
                                   ('محوطه حوزه هنری', 'محوطه حوزه هنری'),
                                   ('روبروی مسجد حضرت آیت الله خامنه ای', 'روبروی مسجد حضرت آیت الله خامنه ای'), ('گالری شماره 1 خانه عکاسان ایران', 'گالری شماره 1 خانه عکاسان ایران'),
                                   ('کارگاه مجسمه سازی', 'کارگاه مجسمه سازی'),
                                   ('مسجد حضرت آیت الله خامنه ای', 'مسجد حضرت آیت الله خامنه ای'), ('خانه عکاسان', 'خانه عکاسان'), ('مرکز آفرینش های ادبی', 'مرکز آفرینش های ادبی'),
                                   ('مرکز موسیقی', 'مرکز موسیقی'),
                                   ('مرکز پایداری', 'مرکز پایداری'),
                                   ('مرکز معماری', 'مرکز معماری'), ('مرکز طنز', 'مرکز طنز'), ('مرکز هنرهای نمایشی', 'مرکز هنرهای نمایشی')
                                    , ('مرکز روابط عمومی', 'مرکز روابط عمومی')])
    level = StringField(validators=[DataRequired()])
    office = StringField(validators=[DataRequired()])
    achievements = TextAreaField(validators=[DataRequired()])
    meh_moh1 = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    meh_moh2 = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    meh_moh3 = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class multimedia_form(Form):
    name = StringField(validators=[DataRequired()])
    frame = SelectField(choices=[('آنونس', 'آنونس'), ('تیزر', 'تیزر'),('فتوکلیپ', 'فتوکلیپ'), ('مستند', 'مستند'),('وله', 'وله'), ('کلیپ', 'کلیپ')])
    center = StringField(validators=[DataRequired()])
    used_place = SelectField(choices=[('داخلی', 'داخلی'), ('خارجی', 'خارجی')])
    producted_place = SelectField(choices=[('داخلی', 'داخلی'), ('خارجی', 'خارجی')])
    product_time = StringField(validators=[DataRequired()])
    used = StringField(validators=[DataRequired()])
    meh_moh = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    description = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class library_enghelab_form(Form):
    ex_subjects_number = StringField(validators=[DataRequired()])
    ex_resource_number = StringField(validators=[DataRequired()])
    ex_digital_resource_number = StringField(validators=[DataRequired()])
    ex_pn_resource_number = SelectField(choices=[('داخلی', 'داخلی'), ('خارجی', 'خارجی')])
    lang1 = SelectField(choices=[('فارسی', 'فارسی'), ('عربی', 'عربی'),('لاتین', 'لاتین')])
    lang2 = SelectField(choices=[('فارسی', 'فارسی'), ('عربی', 'عربی'),('لاتین', 'لاتین')])
    lang3 = SelectField(choices=[('فارسی', 'فارسی'), ('عربی', 'عربی'),('لاتین', 'لاتین')])
    new_subjects_number = StringField(validators=[DataRequired()])
    new_resource_number = StringField(validators=[DataRequired()])
    new_digital_resource_number = StringField(validators=[DataRequired()])
    new_pn_resource_number = StringField(validators=[DataRequired()])
    couns_pn_number = StringField(validators=[DataRequired()])
    couns_research_proj_number = StringField(validators=[DataRequired()])
    pn_subjects_number = StringField(validators=[DataRequired()])
    lib_members_number = StringField(validators=[DataRequired()])
    lib_members_number_thisYear = StringField(validators=[DataRequired()])
    lib_members_women = StringField(validators=[DataRequired()])
    lib_members_men = TextAreaField(validators=[DataRequired()])
    lib_members_diplom = StringField(validators=[DataRequired()])
    lib_members_kardani = StringField(validators=[DataRequired()])
    lib_members_karshenasi = StringField(validators=[DataRequired()])
    lib_members_doctori = StringField(validators=[DataRequired()])
    borrowed_book_number = StringField(validators=[DataRequired()])
    borrowed_nash_number = StringField(validators=[DataRequired()])
    borrowed_digital_number = StringField(validators=[DataRequired()])
    borrowed_pn_number = StringField(validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class library_jang_form(Form):
    ex_subjects_number = StringField(validators=[DataRequired()])
    ex_resource_number = StringField(validators=[DataRequired()])
    ex_digital_resource_number = StringField(validators=[DataRequired()])
    ex_pn_resource_number = SelectField(choices=[('داخلی', 'داخلی'), ('خارجی', 'خارجی')])
    lang1 = SelectField(choices=[('فارسی', 'فارسی'), ('عربی', 'عربی'),('لاتین', 'لاتین')])
    lang2 = SelectField(choices=[('فارسی', 'فارسی'), ('عربی', 'عربی'),('لاتین', 'لاتین')])
    lang3 = SelectField(choices=[('فارسی', 'فارسی'), ('عربی', 'عربی'),('لاتین', 'لاتین')])
    new_subjects_number = StringField(validators=[DataRequired()])
    new_resource_number = StringField(validators=[DataRequired()])
    new_digital_resource_number = StringField(validators=[DataRequired()])
    new_pn_resource_number = StringField(validators=[DataRequired()])
    couns_pn_number = StringField(validators=[DataRequired()])
    couns_research_proj_number = StringField(validators=[DataRequired()])
    pn_subjects_number = StringField(validators=[DataRequired()])
    lib_members_number = StringField(validators=[DataRequired()])
    lib_members_number_thisYear = StringField(validators=[DataRequired()])
    lib_members_women = StringField(validators=[DataRequired()])
    lib_members_men = TextAreaField(validators=[DataRequired()])
    lib_members_diplom = StringField(validators=[DataRequired()])
    lib_members_kardani = StringField(validators=[DataRequired()])
    lib_members_karshenasi = StringField(validators=[DataRequired()])
    lib_members_doctori = StringField(validators=[DataRequired()])
    borrowed_book_number = StringField(validators=[DataRequired()])
    borrowed_nash_number = StringField(validators=[DataRequired()])
    borrowed_digital_number = StringField(validators=[DataRequired()])
    borrowed_pn_number = StringField(validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class result_review_form(Form):
    kar_num = StringField(validators=[DataRequired()])
    accepted_num = StringField(validators=[DataRequired()])
    show_kind = StringField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class bachelor_poem(Form):
    sent_asar = StringField(validators=[DataRequired()])
    seen_asar_num = StringField(validators=[DataRequired()])
    collections_num = StringField(validators=[DataRequired()])
    one_asar_num = StringField(validators=[DataRequired()])
    sent_to_mehr_asar_num = StringField(validators=[DataRequired()])
    sent_to_city_asar_num = StringField(validators=[DataRequired()])
    printed_num = StringField(validators=[DataRequired()])
    in_printed_num = StringField(validators=[DataRequired()])
    rejected_num = StringField(validators=[DataRequired()])
    famous_persons = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class plato_form(Form):
    group_name = StringField(validators=[DataRequired()])
    director = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    clock_num = StringField(validators=[DataRequired()])
    program_kind = SelectField(choices=[('اجرای عمومی', 'اجرای عمومی'), ('جشنواره داخلی', 'جشنواره داخلی'), ('جشنواره مشارکت', 'جشنواره مشارکت')])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class visual_products_form(Form):
    major_name = StringField(validators=[DataRequired()])
    number = StringField(validators=[DataRequired()])
    producers_name = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class music_products_form(Form):
    music_name = StringField(validators=[DataRequired()])
    outing_pos = StringField(validators=[DataRequired()])
    outing_turn = StringField(validators=[DataRequired()])
    frame = StringField(validators=[DataRequired()])
    music_kind = StringField(validators=[DataRequired()])
    singer = StringField(validators=[DataRequired()])
    music_producer = StringField(validators=[DataRequired()])
    tirax = StringField(validators=[DataRequired()])
    meh_moh = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class research_form(Form):
    research_name = StringField(validators=[DataRequired()])
    author = StringField(validators=[DataRequired()])
    research_subject = StringField(validators=[DataRequired()])
    outing_place = StringField(validators=[DataRequired()])
    meh_moh = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class exhibitions_form(Form):
    name = StringField(validators=[DataRequired()])
    show_subject = StringField(validators=[DataRequired()])
    os_city = SelectField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'),
                                   ('اصفهان', 'اصفهان'), ('البرز', 'البرز'),
                                   ('ایلام', 'ایلام'),
                                   ('بوشهر', 'بوشهر'), ('تهران', 'تهران'),
                                   ('چهارمحال بختیاری', 'چهارمحال بختیاری'),
                                   ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'),
                                   ('خراسان شمالی', 'خراسان شمالی'),
                                   ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'),
                                   ('سمنان', 'سمنان'),
                                   ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'),
                                   ('قم', 'قم'),
                                   ('کردستان', 'کردستان'),
                                   ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهکیلویه و بویراحمد', 'کهکیلویه و بویراحمد'),
                                   ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'),
                                   ('مازندران', 'مازندران'),
                                   ('مرکزی', 'مرکزی'),
                                   ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'),
                                   ('یزد', 'یزد')])
    city = StringField(validators=[DataRequired()])
    contact_num = StringField(validators=[DataRequired()])
    meh_moh = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    finish_date_day = SelectField(choices=[(i, i) for i in range(1, 32)])
    finish_date_month = SelectField(choices=[(i, i) for i in range(1, 13)])
    finish_date_year = SelectField(choices=[(i, i) for i in range(1385, 1411)])
    description  = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class congress_form(Form):
    name = StringField(validators=[DataRequired()])
    office = SelectField(choices=[('خانه عکاسان','خانه عکاسان'), ('روابط عمومی','روابط عمومی'), ('موسسه سپهر سوره مهر','موسسه سپهر سوره مهر'),
                                    ('مرکز آفرینش های ادبی','مرکز آفرینش های ادبی'), ('مرکز تجسمی','مرکز تجسمی'), ('مرکز ترجمه','مرکز ترجمه'),
                                    ('مرکز طنز','مرکز طنز'), ('مرکز مطالعات و تحقیقات فرهنگ و ادب پایداری', 'مرکز مطالعات و تحقیقات فرهنگ و ادب پایداری'), ('مرکز معماری', 'مرکز معماری'),
                                    ('مرکز موسیقی', 'مرکز موسیقی'), ('مرکز هنرهای نمایشی', 'مرکز هنرهای نمایشی'), ('کودک و نوجوان', 'کودک و نوجوان')])
    contact_num = StringField(validators=[DataRequired()])
    contact_pos = StringField(validators=[DataRequired()])
    country = StringField(validators=[DataRequired()])
    city = SelectField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'),
                                   ('اصفهان', 'اصفهان'), ('البرز', 'البرز'),
                                   ('ایلام', 'ایلام'),
                                   ('بوشهر', 'بوشهر'), ('تهران', 'تهران'),
                                   ('چهارمحال بختیاری', 'چهارمحال بختیاری'),
                                   ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'),
                                   ('خراسان شمالی', 'خراسان شمالی'),
                                   ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'),
                                   ('سمنان', 'سمنان'),
                                   ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'),
                                   ('قم', 'قم'),
                                   ('کردستان', 'کردستان'),
                                   ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهکیلویه و بویراحمد', 'کهکیلویه و بویراحمد'),
                                   ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'),
                                   ('مازندران', 'مازندران'),
                                   ('مرکزی', 'مرکزی'),
                                   ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'),
                                   ('یزد', 'یزد')])
    salon = SelectField(choices=[('سالن اوستا', 'سالن اوستا'), ('سالن کنفرانس حوزه ریاست', 'سالن کنفرانس حوزه ریاست'), ('سالن ابوالفضل عالی', 'سالن ابوالفضل عالی'),
                                   ('سالن کنفرانس پژوهشگاه', 'سالن کنفرانس پژوهشگاه'), ('سالن سلمان هراتی', 'سالن سلمان هراتی'),
                                   ('تالار سوره', 'تالار سوره'),
                                   ('گالری شماره 2 خانه عکاسان ایران', 'گالری شماره 2 خانه عکاسان ایران'), ('سالن استاد امیرحسین فردی', 'سالن استاد امیرحسین فردی'),
                                   ('تالار اندیشه', 'تالار اندیشه'),
                                   ('تالار مهر', 'تالار مهر'), ('تالار ماه', 'تالار ماه'),
                                   ('محوطه حوزه هنری', 'محوطه حوزه هنری'),
                                   ('روبروی مسجد حضرت آیت الله خامنه ای', 'روبروی مسجد حضرت آیت الله خامنه ای'), ('گالری شماره 1 خانه عکاسان ایران', 'گالری شماره 1 خانه عکاسان ایران'),
                                   ('کارگاه مجسمه سازی', 'کارگاه مجسمه سازی'),
                                   ('مسجد حضرت آیت الله خامنه ای', 'مسجد حضرت آیت الله خامنه ای'), ('خانه عکاسان', 'خانه عکاسان'), ('مرکز آفرینش های ادبی', 'مرکز آفرینش های ادبی'),
                                   ('مرکز موسیقی', 'مرکز موسیقی'),
                                   ('مرکز پایداری', 'مرکز پایداری'),
                                   ('مرکز معماری', 'مرکز معماری'), ('مرکز طنز', 'مرکز طنز'), ('مرکز هنرهای نمایشی', 'مرکز هنرهای نمایشی')
                                    , ('مرکز روابط عمومی', 'مرکز روابط عمومی')])
    frame = StringField(validators=[DataRequired()])
    meh_moh = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    famous_persons = TextAreaField(validators=[DataRequired()])
    sokhanrans = TextAreaField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class bought_photos_form(Form):
    photo_subject = StringField(validators=[DataRequired()])
    number = StringField(validators=[DataRequired()])
    tar_ghar = StringField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class bachelor_written(Form):
    kar_number = StringField(validators=[DataRequired()])
    accepted_number = StringField(validators=[DataRequired()])
    frame = SelectField(choices=[('پژوهش', 'پژوهش'), ('نمایشنامه', 'نمایشنامه')])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class festivals_detailed_form(Form):
    name = StringField(validators=[DataRequired()])
    subject = StringField(validators=[DataRequired()])
    art_dab = StringField(validators=[DataRequired()])
    all_asar = StringField(validators=[DataRequired()])
    take_parted_person = StringField(validators=[DataRequired()])
    os_city = SelectField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'),
                                   ('اصفهان', 'اصفهان'), ('البرز', 'البرز'),
                                   ('ایلام', 'ایلام'),
                                   ('بوشهر', 'بوشهر'), ('تهران', 'تهران'),
                                   ('چهارمحال بختیاری', 'چهارمحال بختیاری'),
                                   ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'),
                                   ('خراسان شمالی', 'خراسان شمالی'),
                                   ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'),
                                   ('سمنان', 'سمنان'),
                                   ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'),
                                   ('قم', 'قم'),
                                   ('کردستان', 'کردستان'),
                                   ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهکیلویه و بویراحمد', 'کهکیلویه و بویراحمد'),
                                   ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'),
                                   ('مازندران', 'مازندران'),
                                   ('مرکزی', 'مرکزی'),
                                   ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'),
                                   ('یزد', 'یزد')])
    city = StringField(validators=[DataRequired()])
    finished_asar = StringField(validators=[DataRequired()])
    salon = SelectField(choices=[('سالن اوستا', 'سالن اوستا'), ('سالن کنفرانس حوزه ریاست', 'سالن کنفرانس حوزه ریاست'), ('سالن ابوالفضل عالی', 'سالن ابوالفضل عالی'),
                                   ('سالن کنفرانس پژوهشگاه', 'سالن کنفرانس پژوهشگاه'), ('سالن سلمان هراتی', 'سالن سلمان هراتی'),
                                   ('تالار سوره', 'تالار سوره'),
                                   ('گالری شماره 2 خانه عکاسان ایران', 'گالری شماره 2 خانه عکاسان ایران'), ('سالن استاد امیرحسین فردی', 'سالن استاد امیرحسین فردی'),
                                   ('تالار اندیشه', 'تالار اندیشه'),
                                   ('تالار مهر', 'تالار مهر'), ('تالار ماه', 'تالار ماه'),
                                   ('محوطه حوزه هنری', 'محوطه حوزه هنری'),
                                   ('روبروی مسجد حضرت آیت الله خامنه ای', 'روبروی مسجد حضرت آیت الله خامنه ای'), ('گالری شماره 1 خانه عکاسان ایران', 'گالری شماره 1 خانه عکاسان ایران'),
                                   ('کارگاه مجسمه سازی', 'کارگاه مجسمه سازی'),
                                   ('مسجد حضرت آیت الله خامنه ای', 'مسجد حضرت آیت الله خامنه ای'), ('خانه عکاسان', 'خانه عکاسان'), ('مرکز آفرینش های ادبی', 'مرکز آفرینش های ادبی'),
                                   ('مرکز موسیقی', 'مرکز موسیقی'),
                                   ('مرکز پایداری', 'مرکز پایداری'),
                                   ('مرکز معماری', 'مرکز معماری'), ('مرکز طنز', 'مرکز طنز'), ('مرکز هنرهای نمایشی', 'مرکز هنرهای نمایشی')
                                    , ('مرکز روابط عمومی', 'مرکز روابط عمومی')])
    choosing_asar_team = StringField(validators=[DataRequired()])
    referees = StringField(validators=[DataRequired()])
    asar_parted_num = StringField(validators=[DataRequired()])
    international_rec = TextAreaField(validators=[DataRequired()])
    area_rec = TextAreaField(validators=[DataRequired()])
    asar_parted_in_dif = TextAreaField(validators=[DataRequired()])
    women = StringField(validators=[DataRequired()])
    men = StringField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class letters_form(Form):
    result_kind = RadioField('نوع اثر', choices=[('کتاب', 'کتاب'), ('نشریه', 'نشریه')])
    back = SubmitField('بازگشت')
    logout = SubmitField('خروج')
    continues = SubmitField('ادامه')


class book_form(Form):
    name = StringField(validators=[DataRequired()])
    author = StringField(validators=[DataRequired()])
    translator = StringField(validators=[DataRequired()])
    nasher = StringField(validators=[DataRequired()])
    lang = StringField(validators=[DataRequired()])
    print_turn = StringField(validators=[DataRequired()])
    sub_frame = StringField(validators=[DataRequired()])
    roo_bar = BooleanField()
    nasher_city = SelectField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'),
                                   ('اصفهان', 'اصفهان'), ('البرز', 'البرز'),
                                   ('ایلام', 'ایلام'),
                                   ('بوشهر', 'بوشهر'), ('تهران', 'تهران'),
                                   ('چهارمحال بختیاری', 'چهارمحال بختیاری'),
                                   ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'),
                                   ('خراسان شمالی', 'خراسان شمالی'),
                                   ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'),
                                   ('سمنان', 'سمنان'),
                                   ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'),
                                   ('قم', 'قم'),
                                   ('کردستان', 'کردستان'),
                                   ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهکیلویه و بویراحمد', 'کهکیلویه و بویراحمد'),
                                   ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'),
                                   ('مازندران', 'مازندران'),
                                   ('مرکزی', 'مرکزی'),
                                   ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'),
                                   ('یزد', 'یزد')])
    meh_moh = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    shomargan_num = StringField(validators=[DataRequired()])
    pages = StringField(validators=[DataRequired()])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')


class journal_form(Form):
    name = StringField(validators=[DataRequired()])
    head_name = StringField(validators=[DataRequired()])
    print_turn = StringField(validators=[DataRequired()])
    shomargan_num = StringField(validators=[DataRequired()])
    pages = StringField(validators=[DataRequired()])
    frame = StringField(validators=[DataRequired()])
    roo_bar = BooleanField()
    nasher_city = SelectField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'),
                                   ('اصفهان', 'اصفهان'), ('البرز', 'البرز'),
                                   ('ایلام', 'ایلام'),
                                   ('بوشهر', 'بوشهر'), ('تهران', 'تهران'),
                                   ('چهارمحال بختیاری', 'چهارمحال بختیاری'),
                                   ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'),
                                   ('خراسان شمالی', 'خراسان شمالی'),
                                   ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'),
                                   ('سمنان', 'سمنان'),
                                   ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'),
                                   ('قم', 'قم'),
                                   ('کردستان', 'کردستان'),
                                   ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهکیلویه و بویراحمد', 'کهکیلویه و بویراحمد'),
                                   ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'),
                                   ('مازندران', 'مازندران'),
                                   ('مرکزی', 'مرکزی'),
                                   ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'),
                                   ('یزد', 'یزد')])
    festival_name = StringField(validators=[DataRequired()])
    meh_moh = SelectField(choices=[('بیداری اسلامی', 'بیداری اسلامی'), ('پایداری', 'پایداری'), ('حجاب و عفاف', 'حجاب و عفاف'),
                                   ('دفاع مقدس', 'دفاع مقدس'), ('سبک زندگی ایرانی اسلامی', 'سبک زندگی ایرانی اسلامی'),
                                   ('مدیریت جهادی و اقتصاد مقاومتی', 'مدیریت جهادی و اقتصاد مقاومتی'),
                                   ('مکارم اخلاقی و اخلاق مداری', 'مکارم اخلاقی و اخلاق مداری'), ('کودک و نوجوان', 'کودک و نوجوان')])
    back = SubmitField('بازگشت')
    add = SubmitField('ثبت')
    logout = SubmitField('خروج')
