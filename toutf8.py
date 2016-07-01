# from bs4 import BeautifulSoup
# from bs4 import UnicodeDammit
# import chardet



def remove_silly_smart_quotes(path_list):
    for path in path_list:
        with open(path, "rb") as f:
            file = f.read()
        file = file.replace(b"\xef\xbf\xbd", b"'").decode('utf-8')
        with open(path, "w") as f:
            f.write(file)

remove_silly_smart_quotes(["iConference_edited/iConf2008t.txt"])

# NOTES
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# try #4:
    # IT WORKS!
    # Microsoft please go die : )

# "iConference/iConf2008t_test.txt"
# """
# <author> Mathiesen, Kay
# <title> Indigenous Peoples� Rights to Culture and Individual Rights to Access
# <abstract> Using the methods of philosophical analysis and concepts from moral and political philosophy Indigenous Peoples� human right to control access to their cultural information is defended. The concept of a �right� is delineated and different types of rights are differentiated. The method of an �overlapping consensus� is used. In attempting to articulate the moral foundation for Indigenous Peoples� rights to culture, we can start with justifications for limiting access that are already widely accepted within our society. These widely accepted justifications for controlling or limiting access to information include the claim that said information is (a) under copyright, (b) a trade or state secret, (c) harmful to some segment of society, or is (d) private or confidential. The moral grounds for each of these limitations on free access is explored. (a)-(c) are found to not provide an adequate ground for Indigenous People�s rights to control access to their culture. The cultural rights of Indigenous Peoples are defended as a form of group privacy. Two possible moral dangers of this defense of indigenous peoples rights to culture are considered. It is shown that on a properly nuanced understanding of the contours of the Indigenous Peoples� rights to group privacy, they do not give rise to either of these dangers.
#
# <author> Choi, Heekyung
# <title> �Just Me in a Closet with a Computer�: Student Perceptions of Undergraduate Information Technology Programs
# <abstract> Many institutions of higher education in the US are offering an information technology (IT) education program at an undergraduate level. So far, not many studies about this young academic program have explored students� perspectives. Students� perspectives are important input for educators to implement an IT education program that properly addresses students� needs. This study has investigated college students� perceptions and expectations for formal IT education in college through in-depth qualitative interviews. Interviewees were college students who were enrolled in courses offered from an IT minor program. This study has revealed that many college students feel that there is a void in college education in dealing with issues emerging from recent developments of IT. The interviewees indicated that the existing computer science program did not satisfy their needs. Students perceived that IT is something that they would have to confront in their future, and sought IT education regardless of their fondness for using and learning IT. By taking the IT minor, students tried to supplement their knowledge in their major and be better prepared for the fields that they would pursue after graduation.
#
# <author> Mokros, Hartmut B.
# <title> One iSchool's Ideas and Identity: Doctoral Training and Research at Rutgers-SCILS 1959-2007
# <abstract> The proposed paper for presentation at the Third iConference addresses the �Nature and Scope of iSchools and iResearch� conference theme. It addresses this theme through report of an in-depth case study of the organizational, social, and intellectual evolution of one early pioneer in the iSchool movement, the Rutgers University School of Communication, Information, and Library Studies (SCILS). The paper first situates SCILS within the iSchool movement, examining its commonalities with and uniqueness from other members of the iSchool Caucus. Thereafter, the paper focuses specifically on the evolution of doctoral research and training, beginning with the program�s development as a disciplinary LIS program, followed by its transformation into an interdisciplinary program with the multidisciplinary merger that founded SCILS in 1982. The paper examines the evolution of ideas developed in dissertation research produced before and after the founding of SCILS interdisciplinary doctoral program in 1987. This includes analysis of the 269 dissertation produced in the program from 1961 to 2007. It compares and contrasts these periods in terms of ideas, methods and the influence played by dissertation supervisors (44 in all). Finally, it examines the influence of key organizational changes on the perceived identity of the school, its relationship with external constituencies, and its intellectual vision into the future.
# """

# with open("iConference/iConf2008t_test.txt", mode = "rb") as f:
#     file = f.read()
#
# print(file)
#
# file1 = file.replace(b"\xef\xbf\xbd", b"'")
# file1 = file1.decode('utf-8')
#
# print(file1)
#
# with open("iConference/iConf2008t_test1.txt", mode = "w") as f:
#     f.write(file1)

# ++++++++++++

# try #1:
    # can't read original text on mac(pycharm, textwrangler, atom, and other IDEs)
    # try manually: text encoding detected by atom as windows1252
    # can read text now
    # text copied from atom and saved as utf8 file with smart quotes
    # try to remove silly smart quotes with .replace, didn't work
    # even it worked this would not be automatic enough, human work involved, time wasted
    # should find ways to automatically change files from windows1252 to utf8 or unicode, and
    #   remove awkward characters caused by smart quotes

# "iConference_edited/test.txt"
# """
# <author> Mathiesen, Kay
# <title> Indigenous Peoples’ Rights to Culture and Individual Rights to Access
# <abstract> Using the methods of philosophical analysis and concepts from moral and political philosophy Indigenous Peoples’ human right to control access to their cultural information is defended. The concept of a “right” is delineated and different types of rights are differentiated. The method of an “overlapping consensus” is used. In attempting to articulate the moral foundation for Indigenous Peoples’ rights to culture, we can start with justifications for limiting access that are already widely accepted within our society. These widely accepted justifications for controlling or limiting access to information include the claim that said information is (a) under copyright, (b) a trade or state secret, (c) harmful to some segment of society, or is (d) private or confidential. The moral grounds for each of these limitations on free access is explored. (a)-(c) are found to not provide an adequate ground for Indigenous People’s rights to control access to their culture. The cultural rights of Indigenous Peoples are defended as a form of group privacy. Two possible moral dangers of this defense of indigenous peoples rights to culture are considered. It is shown that on a properly nuanced understanding of the contours of the Indigenous Peoples’ rights to group privacy, they do not give rise to either of these dangers.
#
# <author> Krishnamurthy, Prashant
# <title> Information Dissemination and Information Assurance in Vehicular Networks: A Survey
# <abstract> Vehicular networks aimed toward providing roadside services such as traffic alerts, estimated time to reach a destination, alternative routes, and in general improve the efficiency and safety on the road are emerging in both the United States and Europe. Information exchange in such networks occurs between vehicles (inter-vehicle communications) in an ad hoc manner and also with roadside base stations using so-called dedicated short range communication links. Research on technology related to vehicular networks is being conducted by many universities and is being widely reported in the mainstream media as well. Vehicular networks are thus expected to become an important part of community networks of the future. In this paper we will survey the different types of dissemination of information and the assurance of such information in vehicular networks. The paper will discuss the architecture of vehicular networks, classify different types of information exchange (safety, traffic related, and content) and different methods of information exchange (opportunistic exchange of resources between vehicles, vehicle assisted data delivery, cooperative downloading of information, etc.). Then we discuss information assurance issues in vehicular networks and survey the solutions proposed for ensuring authenticity/integrity of information, location privacy of vehicles, eviction of faulty or misbehaving vehicles from the information network (e.g., using reputation), etc.
#
# <author> Sarmiento, Johann; Stahl, Gerrry
# <title> Information Practices to Sustain Knowledge Building: The Case of the Virtual Math Teams Online Community
# <abstract> The sustained knowledge building of virtual groups and online communities requires that coparticipants overcome a wide range of gaps in their interactions, especially in the context of long-term activity across multiple episodes and collectivities. Here we present an analysis of the collective information practices of virtual teams engaged in collaborative problem-solving as part of the Virtual Math Teams (VMT) online community. Our analysis aimed at understanding the information practices that teams employed to bridged the apparent discontinuity of their collaborative interactions (e.g. multiple collaborative sessions, teams, and problem tasks) and exploring the role that such bridging activity plays in their knowledge building over time.
#
# <author> Choi, Heekyung
# <title> “Just Me in a Closet with a Computer”: Student Perceptions of Undergraduate Information Technology Programs
# <abstract> Many institutions of higher education in the US are offering an information technology (IT) education program at an undergraduate level. So far, not many studies about this young academic program have explored students’ perspectives. Students’ perspectives are important input for educators to implement an IT education program that properly addresses students’ needs. This study has investigated college students’ perceptions and expectations for formal IT education in college through in-depth qualitative interviews. Interviewees were college students who were enrolled in courses offered from an IT minor program. This study has revealed that many college students feel that there is a void in college education in dealing with issues emerging from recent developments of IT. The interviewees indicated that the existing computer science program did not satisfy their needs. Students perceived that IT is something that they would have to confront in their future, and sought IT education regardless of their fondness for using and learning IT. By taking the IT minor, students tried to supplement their knowledge in their major and be better prepared for the fields that they would pursue after graduation.
# """

# with open("iConference_edited/test.txt", mode = "r") as f:
#     silly_Microsoft_and_smart_quotes = f.read()
#
# r = silly_Microsoft_and_smart_quotes.replace('“','"').replace('”','"').replace("’", "'")
# print(silly_Microsoft_and_smart_quotes)



# ++++++++++++

# try #2:
    # deal with original text
    # use python built-in functions
    # tried to open in "rb" mode, f.decode("windows-1252"), it should have worked... damn microsoft
    # tried f.decode("cp1252"), didn't work

# "iConference/iConf2008t_test.txt"
# """
# <author> Mathiesen, Kay
# <title> Indigenous Peoples� Rights to Culture and Individual Rights to Access
# <abstract> Using the methods of philosophical analysis and concepts from moral and political philosophy Indigenous Peoples� human right to control access to their cultural information is defended. The concept of a �right� is delineated and different types of rights are differentiated. The method of an �overlapping consensus� is used. In attempting to articulate the moral foundation for Indigenous Peoples� rights to culture, we can start with justifications for limiting access that are already widely accepted within our society. These widely accepted justifications for controlling or limiting access to information include the claim that said information is (a) under copyright, (b) a trade or state secret, (c) harmful to some segment of society, or is (d) private or confidential. The moral grounds for each of these limitations on free access is explored. (a)-(c) are found to not provide an adequate ground for Indigenous People�s rights to control access to their culture. The cultural rights of Indigenous Peoples are defended as a form of group privacy. Two possible moral dangers of this defense of indigenous peoples rights to culture are considered. It is shown that on a properly nuanced understanding of the contours of the Indigenous Peoples� rights to group privacy, they do not give rise to either of these dangers.
#
# <author> Choi, Heekyung
# <title> �Just Me in a Closet with a Computer�: Student Perceptions of Undergraduate Information Technology Programs
# <abstract> Many institutions of higher education in the US are offering an information technology (IT) education program at an undergraduate level. So far, not many studies about this young academic program have explored students� perspectives. Students� perspectives are important input for educators to implement an IT education program that properly addresses students� needs. This study has investigated college students� perceptions and expectations for formal IT education in college through in-depth qualitative interviews. Interviewees were college students who were enrolled in courses offered from an IT minor program. This study has revealed that many college students feel that there is a void in college education in dealing with issues emerging from recent developments of IT. The interviewees indicated that the existing computer science program did not satisfy their needs. Students perceived that IT is something that they would have to confront in their future, and sought IT education regardless of their fondness for using and learning IT. By taking the IT minor, students tried to supplement their knowledge in their major and be better prepared for the fields that they would pursue after graduation.
#
# <author> Mokros, Hartmut B.
# <title> One iSchool's Ideas and Identity: Doctoral Training and Research at Rutgers-SCILS 1959-2007
# <abstract> The proposed paper for presentation at the Third iConference addresses the �Nature and Scope of iSchools and iResearch� conference theme. It addresses this theme through report of an in-depth case study of the organizational, social, and intellectual evolution of one early pioneer in the iSchool movement, the Rutgers University School of Communication, Information, and Library Studies (SCILS). The paper first situates SCILS within the iSchool movement, examining its commonalities with and uniqueness from other members of the iSchool Caucus. Thereafter, the paper focuses specifically on the evolution of doctoral research and training, beginning with the program�s development as a disciplinary LIS program, followed by its transformation into an interdisciplinary program with the multidisciplinary merger that founded SCILS in 1982. The paper examines the evolution of ideas developed in dissertation research produced before and after the founding of SCILS interdisciplinary doctoral program in 1987. This includes analysis of the 269 dissertation produced in the program from 1961 to 2007. It compares and contrasts these periods in terms of ideas, methods and the influence played by dissertation supervisors (44 in all). Finally, it examines the influence of key organizational changes on the perceived identity of the school, its relationship with external constituencies, and its intellectual vision into the future.
# """

# with open("iConference/iConf2008t.txt", mode = "rb") as f:
#     file = f.read()
#     file = file.decode('windows-1252')

# (some code deleted)

# ++++++++++++

# try #3:
    # deal with original text
    # tried BS4 and chardet libraries
    # didn't work either
    # wonder if I haven't read their documentation carefully

# "iConference/iConf2008t_test.txt"
# """
# <author> Mathiesen, Kay
# <title> Indigenous Peoples� Rights to Culture and Individual Rights to Access
# <abstract> Using the methods of philosophical analysis and concepts from moral and political philosophy Indigenous Peoples� human right to control access to their cultural information is defended. The concept of a �right� is delineated and different types of rights are differentiated. The method of an �overlapping consensus� is used. In attempting to articulate the moral foundation for Indigenous Peoples� rights to culture, we can start with justifications for limiting access that are already widely accepted within our society. These widely accepted justifications for controlling or limiting access to information include the claim that said information is (a) under copyright, (b) a trade or state secret, (c) harmful to some segment of society, or is (d) private or confidential. The moral grounds for each of these limitations on free access is explored. (a)-(c) are found to not provide an adequate ground for Indigenous People�s rights to control access to their culture. The cultural rights of Indigenous Peoples are defended as a form of group privacy. Two possible moral dangers of this defense of indigenous peoples rights to culture are considered. It is shown that on a properly nuanced understanding of the contours of the Indigenous Peoples� rights to group privacy, they do not give rise to either of these dangers.
#
# <author> Choi, Heekyung
# <title> �Just Me in a Closet with a Computer�: Student Perceptions of Undergraduate Information Technology Programs
# <abstract> Many institutions of higher education in the US are offering an information technology (IT) education program at an undergraduate level. So far, not many studies about this young academic program have explored students� perspectives. Students� perspectives are important input for educators to implement an IT education program that properly addresses students� needs. This study has investigated college students� perceptions and expectations for formal IT education in college through in-depth qualitative interviews. Interviewees were college students who were enrolled in courses offered from an IT minor program. This study has revealed that many college students feel that there is a void in college education in dealing with issues emerging from recent developments of IT. The interviewees indicated that the existing computer science program did not satisfy their needs. Students perceived that IT is something that they would have to confront in their future, and sought IT education regardless of their fondness for using and learning IT. By taking the IT minor, students tried to supplement their knowledge in their major and be better prepared for the fields that they would pursue after graduation.
#
# <author> Mokros, Hartmut B.
# <title> One iSchool's Ideas and Identity: Doctoral Training and Research at Rutgers-SCILS 1959-2007
# <abstract> The proposed paper for presentation at the Third iConference addresses the �Nature and Scope of iSchools and iResearch� conference theme. It addresses this theme through report of an in-depth case study of the organizational, social, and intellectual evolution of one early pioneer in the iSchool movement, the Rutgers University School of Communication, Information, and Library Studies (SCILS). The paper first situates SCILS within the iSchool movement, examining its commonalities with and uniqueness from other members of the iSchool Caucus. Thereafter, the paper focuses specifically on the evolution of doctoral research and training, beginning with the program�s development as a disciplinary LIS program, followed by its transformation into an interdisciplinary program with the multidisciplinary merger that founded SCILS in 1982. The paper examines the evolution of ideas developed in dissertation research produced before and after the founding of SCILS interdisciplinary doctoral program in 1987. This includes analysis of the 269 dissertation produced in the program from 1961 to 2007. It compares and contrasts these periods in terms of ideas, methods and the influence played by dissertation supervisors (44 in all). Finally, it examines the influence of key organizational changes on the perceived identity of the school, its relationship with external constituencies, and its intellectual vision into the future.
# """

# with open("iConference/iConf2008t_test.txt", mode = "rb") as f:
#     silly_Microsoft_and_smart_quotes = f.read()
#
#
# print(chardet.detect(silly_Microsoft_and_smart_quotes))
#
# print(silly_Microsoft_and_smart_quotes)
#
# print("\n\n")
#
# iconf = UnicodeDammit(silly_Microsoft_and_smart_quotes, ["windows-1252"], smart_quotes_to="html").unicode_markup
#
# print(iconf)

# ++++++++++++

# other code

# with open("iConference/iConf2008t_test.txt", "rb") as f:
#     file = f.read()
#
# print(file)
# print("\n\n")
#     # new = file.encode('unicode')
#
# filedecode = file.decode("windows-1252")

# print(filedecode)

# with open("iConference_edited/iConf2008t_test_01.txt", "w") as f:
#    f.write(file)


# encoded = data.decode('Windows-1252').encode('utf-8')

# ++++++++++++

# Brilliant, just found only iConf2008t.txt has this windows-1252 problem
# I could have done it manually through find and replace in atom... T_T