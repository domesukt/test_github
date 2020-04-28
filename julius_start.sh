#!/bin/sh

export ALSADEV=plughw:1
#~/julius/julius-4.4.2.1/julius/julius -C ~/julius/julius-kit/dictation-kit-v4.4/main.jconf -C ~/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -lv 300 -module 10500 nostrip
~/julius/julius-4.4.2.1/julius/julius -C ~/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -lv 300 -gram ~/julius/dict/tv_voice -module 10500


echo $! #プロセスIDを出力
sleep 2 #2秒間スリープ