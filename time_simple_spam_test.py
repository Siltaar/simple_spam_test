#!/usr/bin/env python2
# coding: utf-8
# author : Simon Descarpentries
# date: 2017 - 2018
# licence: GPLv3

from doctest import run_docstring_examples
from datetime import datetime
from simple_spam_test import spam_test
from test_simple_spam_test import test_spam_test_theoritical_cases, test_spam_test_real_cases

"""
Intel(R) Xeon(R) CPU           L5420  @ 2.50GHz
Debian 8.9
Python 2.7.9
Python 3.4.2

20171012 3 : 17 tests ; 0.62s ; 0.364ms/t
20171012 2 : 19 tests ; 0.71s ; 0.373ms/t (added 2 real cases)
20171012 3 : 19 tests ; 0.81s ; 0.426ms/t
20171012 2 : 19 tests ; 0.80s ; 0.421ms/t (parse all mail)
20171012 3 : 19 tests ; 0.90s ; 0.473ms/t
20171012 2 : 19 tests ; 0.86s ; 0.452ms/t (check body readability)
20171012 3 : 19 tests ; 0.99s ; 0.521ms/t
20171124 2 : 20 tests ; 1.06s ; 0.530ms/t (check alnum characters)
20171124 3 : 20 tests ; 1.20s ; 0.600ms/t
20171201 2 : 21 tests ; 1,15s ; 0.547ms/t (accept pgp-encrypted stream as valid)
20171201 3 : 21 tests ; 1,33s ; 0.630ms/t
20171220 2 : 22 tests ; 1,48s ; 0.672ms/t (check body wild len against alnum)
20171220 3 : 22 tests ; 1,68s ; 0.763ms/t


Linux 4.9.0-5-amd64 #1 SMP Debian 4.9.65-3+deb9u2 (2018-01-04) x86_64 GNU/Linux
Debian 9.3
Python 2.7.13
Python 3.5.3

20180112 2 : 22 tests ; 1,53s ; 0,695ms/t (check isalpha instead of isalnum)
20180112 3 : 22 tests ; 1,74s ; 0,790ms/t
20180130 2 : 23 tests ; 1,64s ; 0,713ms/t (check bad HTML)
20180130 3 : 23 tests ; 1,87s ; 0,813ms/t
20180314 2 : 23 tests ; 1,70s ; 0,739ms/t (check big HTML, no text, small text…)
20180314 3 : 23 tests ; 1,92s ; 0,834ms/t
20180315 2 : 23 tests ; 1,65s ; 0,717ms/t (no more 'no text' as body len already checked)
20180315 3 : 23 tests ; 1,87s ; 0,813ms/t
20180321 2 : 24 tests ; 1,77s ; 0,737ms/t (separate tests in new file ; slower real testcases…)
20180321 3 : 24 tests ; 2.01s ; 0,837ms/t
20180322 2 : 25 tests ; 1,92s ; 0,768ms/t (body alpha len > 128 ; HTML < 30kc)
20180322 3 : 25 tests ; 2.20s ; 0,880ms/t  - 13%
20180324 2 : 17 tests ; 0.740 ; 0.435ms/t (theoritical cases)
20180324 3 : 17 tests ; 0.797 ; 0.468ms/t  - 8%
20180324 2 :  8 tests ; 1.230 ; 1.537ms/t (real cases)
20180324 3 :  8 tests ; 1.440 ; 1.800ms/t  - 15%
20180326 2 : 26 tests ; 2.05s ; 0,788ms/t (spam if body len < 25 and no HTML part)
20180326 3 : 26 tests ; 2.32s ; 0,892ms/t  - 12%
20180328 2 : 27 tests ; 2.13s ; 0,788ms/t (regexp out badchars ; seeks bad HTML in 10 1st char)
20180328 3 : 27 tests ; 2.43s ; 0,900ms/t  - 12.5%
20180430 2 : 28 tests ; 2.35s ; 0,839ms/t (regexp to count links, if >4 same domain -> +1)
20180430 3 : 28 tests ; 2.72s ; 0,971ms/t  - 13.5%
20180504 2 : 27 tests ; 2.17s ; 0,803mt/t (stop counting recipients)
20180504 3 : 27 tests ; 2.51s ; 0,929mt/t  - 13.5%

"""

startTime = datetime.now()
DEBUG = 0

for i in range(0, 100):
	run_docstring_examples(test_spam_test_theoritical_cases, globals())
	run_docstring_examples(test_spam_test_real_cases, globals())

print(datetime.now() - startTime)
