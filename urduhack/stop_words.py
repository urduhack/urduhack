# coding: utf8
"""
Complete collection of stopwords for the Urdu language.
Maintainer: Ikram Ali(mrikram1989@gmail.com)
version = 2020.02.14
Source = https://github.com/urduhack/urdu-stopwords
"""
from typing import FrozenSet

# Urdu Language Stop words list
STOP_WORDS: FrozenSet[str] = frozenset("""

 آ آئی آئیں آئے آتا آتی آتے آداب آدھ آدھا آدھی آدھے آس آمدید آنا آنسہ آنی آنے
 آپ آگے آہ آہا آیا اب ابھی ابے اتوار ارب اربویں ارے اس اسکا اسکی اسکے اسی اسے اف
 افوہ البتہ الف ان اندر انکا انکی انکے انہوں انہی انہیں اوئے اور
 اوپر اوہو اپ اپنا اپنوں اپنی اپنے اپنےآپ اکثر اگر اگرچہ اگست اہاہا ایسا ایسی ایسے ایک بائیں
 بار بارے بالکل باوجود باہر بج بجے بخیر بشرطیکہ بعد بعض بغیر بلکہ بن بنا بناؤ بند
 بڑی بھر بھریں بھی بہت بہتر بیگم تاکہ تاہم تب تجھ تجھی تجھے ترا تری تلک تم تمام
 تمہارا تمہاروں تمہاری تمہارے تمہیں تو تک تھا تھی تھیں تھے تہائی تیرا تیری تیرے تین جا جاؤ
 جائیں جائے جاتا جاتی جاتے جانی جانے جب جبکہ جدھر جس جسے جن جناب جنہوں جنہیں جو جہاں جی
 جیسا جیسوں جیسی جیسے حالانکہ حالاں حصہ حضرت خاطر خالی خواہ خوب خود دائیں درمیان
 دریں دو دوران دوسرا دوسروں دوسری دوں دکھائیں دگنا دی دیئے دیا دیتا دیتی دیتے دیر دینا دینی
 دینے دیکھو دیں دیے دے ذریعے رکھا رکھتا رکھتی رکھتے رکھنا رکھنی رکھنے رکھو رکھی رکھے رہ رہا
 رہتا رہتی رہتے رہنا رہنی رہنے رہو رہی رہیں رہے ساتھ سامنے ساڑھے سب سبھی سراسر سمیت سوا
 سوائے سکا سکتا سکتے سہ سہی سی سے شاید شکریہ صاحب صاحبہ صرف ضرور طرح طرف طور
 علاوہ عین فقط فلاں فی قبل قطا لئے لائی لائے لاتا لاتی لاتے لانا لانی لانے لایا لو
 لوجی لوگوں لگ لگا لگتا لگتی لگی لگیں لگے لہذا لی لیا لیتا لیتی لیتے لیکن لیں لیے
 لے ماسوا مت مجھ مجھی مجھے محترم محترمہ محترمی محض مرا مرحبا مری مرے مزید مس مسز مسٹر مطابق
 مل منٹ منٹوں مکرمی مگر مگھر مہربانی میرا میروں میری میرے میں نا نزدیک نما نو
 نہ نہیں نیز نیچے نے و وار واسطے واقعی والا والوں والی والے واہ وجہ ورنہ وعلیکم وغیرہ ولے
 وگرنہ وہ وہاں وہی وہیں ویسا ویسے ویں پاس پایا پر پس پلیز پون پونا پونی پونے
 پھر پہ پہر پہلا پہلی پہلے پیر پیچھے چاہئے چاہتے چاہیئے چاہے چلا چلو چلیں چلے چناچہ چند چونکہ
 چوگنی چکی چکیں چکے ڈالنا ڈالنی ڈالنے ڈالے کئے کا کاش کب کبھی کدھر کر
 کرتا کرتی کرتے کرم کرنا کرنے کرو کریں کرے کس کسی کسے کل کم کن کنہیں کو کوئی کون
 کونسا کونسے کچھ کہ کہا کہاں کہہ کہی کہیں کہے کی کیا کیسا کیسے کیونکر کیونکہ کیوں کیے
 کے گئی گئے گا گرما گرمی گنا گو گویا گھنٹا گھنٹوں گھنٹے گی گیا ہائیں ہائے ہاں ہر
 ہرچند ہرگز ہزار ہم ہمارا ہماری ہمارے ہمی ہمیں ہو ہوئی ہوئیں ہوئے ہوا ہوبہو ہوتا تھی ہوتی
 ہوتیں ہوتے ہونا ہونگے ہونی ہونے ہوں ہی ہیلو ہیں ہے یا یات یعنی یک یہ یہاں یہی یہیں


""".split())
