#!/usr/bin/env python
print "======================================================================="
print "1. str.capitalize():"
str = "inovasi tiada henti";
print "str.capitalize():", str.capitalize()
print "======================================================================="
print "2. str.center(width[width[,fillchar]):"
str = "nggak ada tulisan berarti nggak kerja";
print "str.center(50):", str.center(50)
print "======================================================================="
print "3. str.count(sub[,start[,end]]):"
str = "tututlah ilmu sampai ke negeri cina";
sub = "a";
print "str.count(sub, 4, 34):", str.count(sub, 4, 34)
sub = "negeri";
print "str.count(sub) : ", str.count(sub)
print "======================================================================="
print "4. str.find(sub[, start[, end]]):"
str = "manusia baik, manusia yang bermanfaat bagi manusia lainnya";
sub = "baik";
print "str,find(sub, 1, 30):", str.find(sub, 1, 30)
print "======================================================================="
print "5. str.isspace():"
str = "        ";
print "str.isspace():", str.isspace();
str = "metode ini memeriksa apakah string ini hanya terdiri spasi saja?";
print "str.isspace():", str.isspace();
print "======================================================================="
