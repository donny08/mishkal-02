#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        spellcheck
# Purpose:     Arabic spellchecking.
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
import pyarabic.araby as araby

Alphabet = u'ذضصثقفغعهخحجدطكمنتالبيسشظزوةىرؤءئأإآ'
TabReplacment=[
#common spelling error
(araby.ALEF_MAKSURA, araby.YEH),
(araby.TEH_MARBUTA	, araby.HEH),

(araby.ALEF			, araby.ALEF_HAMZA_ABOVE),
(araby.ALEF			, araby.ALEF_HAMZA_BELOW),
(araby.HAMZA			, araby.ALEF_HAMZA_BELOW),
(araby.WAW_HAMZA			, araby.YEH_HAMZA),
(araby.YEH_HAMZA			, araby.WAW_HAMZA),



# o	����� �� ������� shift
# ?	��� ���� ��� �����
# ?	� �
# o	���������� : ���� ��� ��� ����� ���� ������
# ?	� � � � �
# ?	� � �
# ?	� �
# ?	� �
# ?	� �
# ?	� �
# ?	� �
# ?	� �
# ?	� �
# ?	� � 
# o	���������� ����
# ?	� � � � 
# o	������� 
# ?	� � � � � �� �
# o	���������� ����
# ?	����:
# �	� �
# �	� �
# �	� �
# ?	�����
# �	� �
# ?	���
# �	� � 
# �	� �
# �	� �
#common pronciation error
(araby.DAD			, araby.ZAH),
(araby.ZAH			, araby.DAD),
(araby.THAL, 	araby.ZAIN),
(araby.ZAIN,	araby.THAL),
(araby.SEEN,	araby.THEH),
(araby.THEH,	araby.SEEN),
(araby.QAF,	araby.ALEF_HAMZA_ABOVE),
(araby.QAF,	araby.ALEF_HAMZA_BELOW),
(araby.JEEM,	araby.YEH),
(araby.YEH,	araby.JEEM),
(araby.SAD,	araby.SEEN),
(araby.SEEN,	araby.SAD),
(araby.THEH,	araby.TEH),

# o	������� ��������
# ?	� �
# ?	� �
(araby.TEH,			araby.TEH_MARBUTA),
(araby.TEH_MARBUTA,	araby.TEH),
(araby.ALEF_MAKSURA, araby.ALEF),




]