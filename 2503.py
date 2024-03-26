# This code is provided for you to check that you can connect to your remote database and then carry out a simple python command.
# The code relates to the set up tutorial in week 1

import pyodbc

server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk' 
database = 'BEMM459_TLE'
username = 'TLe' 
password = 'SwmZ351+Zu'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=yes;Encrypt=no;')

cursor = cnxn.cursor()

Landlord_Type = '''
INSERT INTO S.Landlord_Type (landlord_type_id, landlord_type_name)
VALUES 
    (1, 'Private properties'),
    (2, 'University accommodation');
'''
# Make the SQL run on the server.
cursor.execute(Landlord_Type)

Landlord = '''
INSERT INTO S.Landlord (landlord_id, landlord_type_id, landlord_first_name, landlord_last_name, landlord_gender, landlord_email, landlord_phone_number)
VALUES 
    (1, 1, 'Levi', 'Sheen', 'Male', 'lsheen0@gmail.com', '07415123456'),
    (2, 1, 'Shem', 'Crecy', 'Male', 'screcy1@gmail.com', '07720987654'),
    (3, 1, 'Tiler', 'Mangham', 'Male', 'tmangham2@gmail.com', '07903456789'),
    (4, 1, 'Barnabas', 'Grassot', 'Male', 'bgrassot3@gmail.com', '07856234567'),
    (5, 2, 'Nottingham Trent', 'University', '', 'admin@ntu.ac.uk', '07540876543'),
    (6, 1, 'Maurizia', 'Cathersides', 'Female', 'mcathersides5@gmail.com', '07624345678'),
    (7, 1, 'Worden', 'Poyzer', 'Male', 'wpoyzer6@gmail.com', '07891654321'),
    (8, 1, 'Zacharia', 'Mustill', 'Male', 'zmustill7@gmail.com', '07980123456'),
    (9, 1, 'Donia', 'Deniscke', 'Female', 'ddeniscke8@gmail.com', '07739987654'),
    (10, 1, 'Van', 'Hand', 'Male', 'vhand9@gmail.com', '07460234567');
'''
# Make the SQL run on the server.
cursor.execute(Landlord)

Residence = '''
INSERT INTO S.Residence (residence_id, landlord_id, is_catered, residence_name, total_rooms_available, is_central_social_space, is_cleaning_provision, residence_postcode)
VALUES
(1, 2, 0, 'Robin''s Nest Residences', 4, 1, 0, 'NG1 1AA'),
(2, 4, 0, 'Sherwood Lodge', 3, 1, 0, 'NG2 2BB'),
(3, 6, 1, 'Trentside Towers', 4, 0, 1, 'NG3 3CC'),
(4, 6, 0, 'Nottingham Student Haven', 3, 1, 1, 'NG4 4DD'),
(5, 5, 0, 'Forest View Apartments', 6, 1, 0, 'NG5 5EE'),
(6, 5, 0, 'Castle Heights Residences', 6, 0, 0, 'NG6 6FF'),
(7, 5, 1, 'Riverside Manor', 6, 1, 1, 'NG7 7GG'),
(8, 5, 0, 'Meadowview Hall', 6, 0, 0, 'NG8 8HH'),
(9, 5, 1, 'Lakeside Living', 6, 0, 0, 'NG9 9II'),
(10, 8, 0, 'Arboretum Court', 4, 1, 1, 'NG1 0JJ');
'''
# Make the SQL run on the server.
cursor.execute(Residence)

Room_Type = '''
INSERT INTO S.Room_Type (room_type_id, room_type)
VALUES 
    (1, 'Single'),
    (2, 'En-suite'),
    (3, 'Studio');
'''

# Execute the SQL command
cursor.execute(Room_Type)

Residence_RoomType = '''
INSERT INTO S.Residence_RoomType (residence_roomtype_id, residence_id, room_type_id, fee)
VALUES 
    (1, 1, 1, 120),
    (2, 1, 2, 150),
    (3, 2, 2, 200),
    (4, 2, 3, 300),
    (5, 3, 1, 150),
    (6, 3, 2, 250),
    (7, 3, 3, 350),
    (8, 4, 1, 120),
    (9, 5, 3, 200),
    (10, 6, 1, 150),
    (11, 6, 2, 180),
    (12, 6, 3, 260),
    (13, 7, 1, 140),
    (14, 7, 2, 180),
    (15, 8, 2, 200),
    (16, 9, 1, 150),
    (17, 9, 3, 300),
    (18, 10, 3, 300);
'''

# Execute the SQL command
cursor.execute(Residence_RoomType)

ContractLength = '''
INSERT INTO S.ContractLength (contract_length_id, contract_length)
VALUES 
    (1, 40),
    (2, 44),
    (3, 51);
'''

# Execute the SQL command
cursor.execute(ContractLength)

Room = '''
INSERT INTO S.Room (room_id, residence_roomtype_id, contract_length_id, room_number)
VALUES 
    (1, 1, 1, '101'),
    (2, 1, 1, '102'),
    (3, 2, 2, '103'),
    (4, 2, 3, '104'),
    (5, 3, 1, '101'),
    (6, 4, 2, '102'),
    (7, 4, 2, '103'),
    (8, 5, 2, '101'),
    (9, 6, 2, '102'),
    (10, 7, 3, '103'),
    (11, 7, 3, '104'),
    (12, 8, 1, '101'),
    (13, 8, 2, '102'),
    (14, 8, 2, '103'),
    (15, 9, 1, '101'),
    (16, 9, 2, '102'),
    (17, 9, 2, '103'),
    (18, 9, 3, '201'),
    (19, 9, 3, '202'),
    (20, 9, 3, '203'),
    (21, 10, 1, '101'),
    (22, 10, 2, '102'),
    (23, 11, 1, '103'),
    (24, 11, 2, '201'),
    (25, 11, 3, '202'),
    (26, 12, 1, '203'),
    (27, 13, 1, '101'),
    (28, 13, 2, '102'),
    (29, 13, 2, '103'),
    (30, 14, 1, '201'),
    (31, 14, 2, '202'),
    (32, 14, 3, '203'),
    (33, 15, 1, '101'),
    (34, 15, 1, '102'),
    (35, 15, 1, '103'),
    (36, 15, 2, '201'),
    (37, 15, 3, '202'),
    (38, 15, 3, '203'),
    (39, 16, 1, '101'),
    (40, 16, 2, '102'),
    (41, 17, 1, '103'),
    (42, 17, 3, '201'),
    (43, 17, 3, '202'),
    (44, 17, 3, '203'),
    (45, 18, 2, '101'),
    (46, 18, 2, '102'),
    (47, 18, 3, '103'),
    (48, 18, 3, '104');
'''

# Execute the SQL command
cursor.execute(Room)

Student = '''
INSERT INTO S.Student (student_id, first_name, last_name, education_level, student_number, personal_email, school_email, student_gender, student_DOB, Nationality)
VALUES 
    (1, 'Terrye', 'Vanezis', 'Presession', 3470320, 'terrye.vanezis@gmail.com', 'terrye.vanezis@ntu.ac.uk', 'Other', '2003-03-15', 'France'),
    (2, 'Faunie', 'Steuart', 'Postgraduate', 2048735, 'faunie.steuart@gmail.com', 'faunie.steuart@ntu.ac.uk', 'Male', '2002-11-28', 'China'),
    (3, 'Vikki', 'Iannello', 'Postgraduate', 5477382, 'vikki.iannello@gmail.com', 'vikki.iannello@ntu.ac.uk', 'Female', '2001-09-07', 'China'),
    (4, 'Kit', 'Gullam', 'Postgraduate', 1574034, 'kit.gullam@gmail.com', 'kit.gullam@ntu.ac.uk', 'Male', '2003-04-23', 'Myanmar'),
    (5, 'Anet', 'Thickin', 'Postgraduate', 1807382, 'anet.thickin@gmail.com', 'anet.thickin@ntu.ac.uk', 'Female', '2002-08-10', 'China'),
    (6, 'Thebault', 'Dodridge', 'Postgraduate', 4371844, 'thebault.dodridge@gmail.com', 'thebault.dodridge@ntu.ac.uk', 'Male', '2001-06-19', 'Sweden'),
    (7, 'Lorilee', 'Tirkin', 'Postgraduate', 5884419, 'lorilee.tirkin@gmail.com', 'lorilee.tirkin@ntu.ac.uk', 'Female', '2003-12-30', 'Tajikistan'),
    (8, 'Renell', 'Furnell', 'Postgraduate', 2318492, 'renell.furnell@gmail.com', 'renell.furnell@ntu.ac.uk', 'Male', '2002-10-04', 'Kenya'),
    (9, 'Crissy', 'Poure', 'Postgraduate', 3594559, 'crissy.poure@gmail.com', 'crissy.poure@ntu.ac.uk', 'Female', '2001-02-18', 'France'),
    (10, 'Richie', 'Symonds', 'Presession', 1786542, 'richie.symonds@gmail.com', 'richie.symonds@ntu.ac.uk', 'Male', '2003-07-25', 'Mexico'),
    (11, 'Andie', 'Fitzsimon', 'Postgraduate', 4757020, 'andie.fitzsimon@gmail.com', 'andie.fitzsimon@ntu.ac.uk', 'Female', '2002-01-12', 'Portugal'),
    (12, 'Erick', 'Feavers', 'Postgraduate', 3549205, 'erick.feavers@gmail.com', 'erick.feavers@ntu.ac.uk', 'Other', '2001-11-03', 'Poland'),
    (13, 'Maribelle', 'Hambling', 'Postgraduate', 4943805, 'maribelle.hambling@gmail.com', 'maribelle.hambling@ntu.ac.uk', 'Female', '2003-05-20', 'Czech Republic'),
    (14, 'Lotta', 'Raistrick', 'Postgraduate', 1977509, 'lotta.raistrick@gmail.com', 'lotta.raistrick@ntu.ac.uk', 'Male', '2002-09-14', 'Poland'),
    (15, 'Diannne', 'Paish', 'Postgraduate', 4825638, 'diannne.paish@gmail.com', 'diannne.paish@ntu.ac.uk', 'Male', '2001-04-01', 'China'),
    (16, 'Steffie', 'Kitteringham', 'Postgraduate', 4114586, 'steffie.kitteringham@gmail.com', 'steffie.kitteringham@ntu.ac.uk', 'Female', '2003-12-09', 'Mexico'),
    (17, 'Auguste', 'Ardley', 'Postgraduate', 4807390, 'auguste.ardley@gmail.com', 'auguste.ardley@ntu.ac.uk', 'Other', '2001-10-26', 'South Africa'),
    (18, 'Kendell', 'Cullivan', 'Postgraduate', 5301521, 'kendell.cullivan@gmail.com', 'kendell.cullivan@ntu.ac.uk', 'Male', '2000-08-17', 'United States'),
    (19, 'Aarika', 'Lodwick', 'Postgraduate', 3590085, 'aarika.lodwick@gmail.com', 'aarika.lodwick@ntu.ac.uk', 'Female', '2002-06-03', 'Tunisia'),
    (20, 'Collie', 'Lowe', 'Postgraduate', 4045276, 'collie.lowe@gmail.com', 'collie.lowe@ntu.ac.uk', 'Other', '2003-03-08', 'Sweden'),
    (21, 'Lynn', 'Hallut', 'Presession', 5164438, 'lynn.hallut@gmail.com', 'lynn.hallut@ntu.ac.uk', 'Other', '2001-09-12', 'Philippines'),
    (22, 'Aggie', 'Nannoni', 'Postgraduate', 2213809, 'aggie.nannoni@gmail.com', 'aggie.nannoni@ntu.ac.uk', 'Female', '2002-07-28', 'Japan'),
    (23, 'Erny', 'Silby', 'Postgraduate', 5647012, 'erny.silby@gmail.com', 'erny.silby@ntu.ac.uk', 'Female', '2000-02-14', 'Guatemala'),
    (24, 'Emilio', 'Miell', 'Postgraduate', 2992918, 'emilio.miell@gmail.com', 'emilio.miell@ntu.ac.uk', 'Male', '2001-10-30', 'Czech Republic'),
    (25, 'Lind', 'Mellmer', 'Postgraduate', 2991071, 'lind.mellmer@gmail.com', 'lind.mellmer@ntu.ac.uk', 'Other', '2003-05-16', 'Germany'),
    (26, 'Yurik', 'McCumskay', 'Postgraduate', 5367521, 'yurik.mccumskay@gmail.com', 'yurik.mccumskay@ntu.ac.uk', 'Female', '2002-01-21', 'Czech Republic'),
    (27, 'Fanni', 'Fernely', 'Postgraduate', 5180481, 'fanni.fernely@gmail.com', 'fanni.fernely@ntu.ac.uk', 'Female', '2001-03-04', 'Indonesia'),
    (28, 'Zsa zsa', 'Lakin', 'Postgraduate', 2300001, 'zsa.zsa.lakin@gmail.com', 'zsa.zsa.lakin@ntu.ac.uk', 'Male', '2003-11-10', 'Philippines'),
    (29, 'Bethina', 'Batchelour', 'Postgraduate', 4087846, 'bethina.batchelour@gmail.com', 'bethina.batchelour@ntu.ac.uk', 'Female', '2001-07-23', 'Russia'),
    (30, 'Klement', 'Barks', 'Postgraduate', 1619299, 'klement.barks@gmail.com', 'klement.barks@ntu.ac.uk', 'Male', '2000-04-06', 'China'),
    (31, 'Oona', 'Cregan', 'Postgraduate', 5967969, 'oona.cregan@gmail.com', 'oona.cregan@ntu.ac.uk', 'Female', '2003-12-13', 'Russia'),
    (32, 'Glynnis', 'Vanner', 'Postgraduate', 1164231, 'glynnis.vanner@gmail.com', 'glynnis.vanner@ntu.ac.uk', 'Male', '2001-08-28', 'China'),
    (33, 'Elvira', 'Pithcock', 'Postgraduate', 1108777, 'elvira.pithcock@gmail.com', 'elvira.pithcock@ntu.ac.uk', 'Female', '2002-06-11', 'Brazil'),
    (34, 'Ario', 'Tinker', 'Postgraduate', 3570463, 'ario.tinker@gmail.com', 'ario.tinker@ntu.ac.uk', 'Female', '2001-02-25', 'Indonesia'),
    (35, 'Krysta', 'Glaisner', 'Postgraduate', 4939535, 'krysta.glaisner@gmail.com', 'krysta.glaisner@ntu.ac.uk', 'Female', '2003-10-02', 'Philippines'),
    (36, 'Brigg', 'Van der Mark', 'Postgraduate', 4320152, 'brigg.van.der.mark@gmail.com', 'brigg.van.der.mark@ntu.ac.uk', 'Male', '2000-12-19', 'Russia'),
    (37, 'Tiebold', 'Giovannacci', 'Postgraduate', 5358727, 'tiebold.giovannacci@gmail.com', 'tiebold.giovannacci@ntu.ac.uk', 'Female', '2002-06-24', 'China'),
    (38, 'Lamar', 'Redhouse', 'Postgraduate', 4911817, 'lamar.redhouse@gmail.com', 'lamar.redhouse@ntu.ac.uk', 'Female', '2003-03-31', 'Colombia'),
    (39, 'Lisabeth', 'Sunnucks', 'Postgraduate', 2771271, 'lisabeth.sunnucks@gmail.com', 'lisabeth.sunnucks@ntu.ac.uk', 'Male', '2001-01-15', 'Indonesia'),
    (40, 'Elita', 'Archley', 'Postgraduate', 5126148, 'elita.archley@gmail.com', 'elita.archley@ntu.ac.uk', 'Female', '2003-09-20', 'Chile'),
    (41, 'Joshua', 'Iggalden', 'Postgraduate', 4762336, 'joshua.iggalden@gmail.com', 'joshua.iggalden@ntu.ac.uk', 'Male', '2000-05-05', 'Philippines'),
    (42, 'Aeriela', 'Stotherfield', 'Postgraduate', 4034392, 'aeriela.stotherfield@gmail.com', 'aeriela.stotherfield@ntu.ac.uk', 'Male', '2001-01-18', 'South Korea'),
    (43, 'Paolina', 'MacDonagh', 'Postgraduate', 3003729, 'paolina.macdonagh@gmail.com', 'paolina.macdonagh@ntu.ac.uk', 'Male', '2002-11-26', 'Canada'),
    (44, 'Georas', 'Grabiec', 'Postgraduate', 3824816, 'georas.grabiec@gmail.com', 'georas.grabiec@ntu.ac.uk', 'Other', '2001-09-09', 'Indonesia'),
    (45, 'Hewett', 'Youster', 'Postgraduate', 2721567, 'hewett.youster@gmail.com', 'hewett.youster@ntu.ac.uk', 'Female', '2003-04-24', 'Czech Republic'),
    (46, 'Opal', 'Smewing', 'Postgraduate', 5650835, 'opal.smewing@gmail.com', 'opal.smewing@ntu.ac.uk', 'Female', '2002-12-08', 'Cuba'),
    (47, 'Waneta', 'Nesterov', 'Undergraduate', 8978288, 'waneta.nesterov@gmail.com', 'waneta.nesterov@ntu.ac.uk', 'Female', '2000-07-20', 'Philippines'),
    (48, 'Merridie', 'Oven', 'Undergraduate', 7164649, 'merridie.oven@gmail.com', 'merridie.oven@ntu.ac.uk', 'Female', '2001-03-06', 'Brazil'),
    (49, 'Arlene', 'De Biasi', 'Undergraduate', 8525334, 'arlene.debiasi@gmail.com', 'arlene.debiasi@ntu.ac.uk', 'Female', '2002-11-12', 'France'),
    (50, 'Myrilla', 'Dumbellow', 'Undergraduate', 9486518, 'myrilla.dumbellow@gmail.com', 'myrilla.dumbellow@ntu.ac.uk', 'Female', '2003-05-28', 'Russia'),
    (51, 'Fabien', 'Jauncey', 'Undergraduate', 6588887, 'fabien.jauncey@gmail.com', 'fabien.jauncey@ntu.ac.uk', 'Female', '2001-10-11', 'Sweden'),
    (52, 'Peadar', 'Karpov', 'Undergraduate', 9545292, 'peadar.karpov@gmail.com', 'peadar.karpov@ntu.ac.uk', 'Male', '2000-04-02', 'Indonesia'),
    (53, 'Ely', 'Cashley', 'Undergraduate', 9891176, 'ely.cashley@gmail.com', 'ely.cashley@ntu.ac.uk', 'Female', '2002-12-17', 'Finland'),
    (54, 'Grant', 'MacIlhargy', 'Undergraduate', 6842928, 'grant.macilhargy@gmail.com', 'grant.macilhargy@ntu.ac.uk', 'Female', '2001-08-01', 'Argentina'),
    (55, 'Hogan', 'Roskell', 'Undergraduate', 6454185, 'hogan.roskell@gmail.com', 'hogan.roskell@ntu.ac.uk', 'Female', '2002-06-14', 'Peru'),
    (56, 'Corney', 'Aucutt', 'Presession', 8271487, 'corney.aucutt@gmail.com', 'corney.aucutt@ntu.ac.uk', 'Male', '2001-02-27', 'Thailand'),
    (57, 'Della', 'Zucker', 'Undergraduate', 9738695, 'della.zucker@gmail.com', 'della.zucker@ntu.ac.uk', 'Female', '2003-11-03', 'Philippines'),
    (58, 'Carena', 'Vasquez', 'Undergraduate', 7637941, 'carena.vasquez@gmail.com', 'carena.vasquez@ntu.ac.uk', 'Male', '2001-09-18', 'Indonesia'),
    (59, 'Jarrid', 'Ransley', 'Undergraduate', 9117688, 'jarrid.ransley@gmail.com', 'jarrid.ransley@ntu.ac.uk', 'Male', '2000-05-03', 'Serbia'),
    (60, 'Merralee', 'Elner', 'Undergraduate', 7986670, 'merralee.elner@gmail.com', 'merralee.elner@ntu.ac.uk', 'Female', '2002-01-20', 'Indonesia'),
    (61, 'Sigfrid', 'Schrir', 'Undergraduate', 8891609, 'sigfrid.schrir@gmail.com', 'sigfrid.schrir@ntu.ac.uk', 'Female', '2003-09-25', 'Poland'),
    (62, 'Hyatt', 'Squibe', 'Undergraduate', 9676569, 'hyatt.squibe@gmail.com', 'hyatt.squibe@ntu.ac.uk', 'Male', '2000-05-10', 'China'),
    (63, 'Aleta', 'Sheehan', 'Undergraduate', 6695711, 'aleta.sheehan@gmail.com', 'aleta.sheehan@ntu.ac.uk', 'Female', '2001-01-25', 'Philippines'),
    (64, 'Rad', 'Rielly', 'Undergraduate', 6815254, 'rad.rielly@gmail.com', 'rad.rielly@ntu.ac.uk', 'Male', '2002-10-03', 'China'),
    (65, 'Anjela', 'Deakins', 'Undergraduate', 8325765, 'anjela.deakins@gmail.com', 'anjela.deakins@ntu.ac.uk', 'Female', '2003-07-16', 'Japan'),
    (66, 'Jecho', 'Troppmann', 'Undergraduate', 7837965, 'jecho.troppmann@gmail.com', 'jecho.troppmann@ntu.ac.uk', 'Female', '2001-03-01', 'China'),
    (67, 'Sabra', 'Bounds', 'Undergraduate', 8807132, 'sabra.bounds@gmail.com', 'sabra.bounds@ntu.ac.uk', 'Male', '2000-11-14', 'France'),
    (68, 'Andrew', 'Everix', 'Undergraduate', 8692108, 'andrew.everix@gmail.com', 'andrew.everix@ntu.ac.uk', 'Male', '2002-09-29', 'Poland'),
    (69, 'Mayor', 'Swanne', 'Undergraduate', 9969729, 'mayor.swanne@gmail.com', 'mayor.swanne@ntu.ac.uk', 'Female', '2001-06-12', 'Mexico'),
    (70, 'Orsa', 'Thurlby', 'Undergraduate', 8973822, 'orsa.thurlby@gmail.com', 'orsa.thurlby@ntu.ac.uk', 'Female', '2003-02-26', 'Sweden'),
    (71, 'Ailee', 'Colomb', 'Undergraduate', 8102786, 'ailee.colomb@gmail.com', 'ailee.colomb@ntu.ac.uk', 'Male', '2002-12-11', 'United States'),
    (72, 'Adriena', 'Wetherald', 'Undergraduate', 6688620, 'adriena.wetherald@gmail.com', 'adriena.wetherald@ntu.ac.uk', 'Female', '2001-08-23', 'Portugal'),
    (73, 'Jorrie', 'Odd', 'Undergraduate', 7912055, 'jorrie.odd@gmail.com', 'jorrie.odd@ntu.ac.uk', 'Male', '2000-04-07', 'Poland'),
    (74, 'Klarika', 'Twitching', 'Undergraduate', 7433258, 'klarika.twitching@gmail.com', 'klarika.twitching@ntu.ac.uk', 'Male', '2002-12-21', 'Morocco'),
    (75, 'Ariadne', 'Mantz', 'Undergraduate', 8716164, 'ariadne.mantz@gmail.com', 'ariadne.mantz@ntu.ac.uk', 'Female', '2001-10-05', 'Argentina'),
    (76, 'Amii', 'Janeczek', 'Undergraduate', 9881126, 'amii.janeczek@gmail.com', 'amii.janeczek@ntu.ac.uk', 'Male', '2003-05-20', 'Ukraine'),
    (77, 'Waylan', 'Astlatt', 'Undergraduate', 8596543, 'waylan.astlatt@gmail.com', 'waylan.astlatt@ntu.ac.uk', 'Male', '2000-01-03', 'Poland'),
    (78, 'Chrissie', 'Moore', 'Undergraduate', 6412291, 'chrissie.moore@gmail.com', 'chrissie.moore@ntu.ac.uk', 'Male', '2001-07-10', 'Peru'),
    (79, 'Susan', 'MacMearty', 'Undergraduate', 6278864, 'susan.macmearty@gmail.com', 'susan.macmearty@ntu.ac.uk', 'Other', '2002-03-25', 'Indonesia'),
    (80, 'Maritsa', 'Million', 'Undergraduate', 6175919, 'maritsa.million@gmail.com', 'maritsa.million@ntu.ac.uk', 'Female', '2000-11-08', 'China');
'''

# Execute the SQL command
cursor.execute(Student)

Student_Residence_Option = '''
INSERT INTO S.Student_Residence_Option (residence_option_id, student_id, residence_roomtype_id, contract_length_id, residence_priority, date_created)
VALUES 
    (1, 1, 1, 3, 1, '2024-02-15 04:20'),
    (2, 1, 2, 1, 2, '2024-02-15 04:20'),
    (3, 1, 3, 2, 3, '2024-02-15 04:20'),
    (4, 3, 2, 3, 1, '2024-02-15 09:35'),
    (5, 3, 5, 1, 2, '2024-02-15 09:35'),
    (6, 3, 6, 3, 3, '2024-02-15 09:35'),
    (7, 9, 4, 2, 1, '2024-02-15 14:50'),
    (8, 9, 8, 2, 2, '2024-02-15 14:50'),
    (9, 9, 9, 1, 3, '2024-02-15 14:50'),
    (10, 14, 3, 1, 1, '2024-02-15 20:05'),
    (11, 14, 11, 3, 2, '2024-02-15 20:05'),
    (12, 14, 12, 3, 3, '2024-02-15 20:05'),
    (13, 20, 5, 2, 1, '2024-02-16 01:20'),
    (14, 20, 14, 2, 2, '2024-02-16 01:20'),
    (15, 20, 15, 1, 3, '2024-02-16 01:20'),
    (16, 24, 16, 3, 1, '2024-02-16 06:35'),
    (17, 24, 17, 1, 2, '2024-02-16 06:35'),
    (18, 24, 18, 2, 3, '2024-02-16 06:35'),
    (19, 28, 1, 3, 1, '2024-02-16 11:50'),
    (20, 28, 10, 1, 2, '2024-02-16 11:50'),
    (21, 28, 15, 2, 3, '2024-02-16 11:50'),
    (22, 30, 4, 3, 1, '2024-02-16 17:05'),
    (23, 30, 12, 2, 2, '2024-02-16 17:05'),
    (24, 30, 18, 1, 3, '2024-02-16 17:05'),
    (25, 32, 7, 2, 1, '2024-02-16 22:20'),
    (26, 32, 8, 3, 2, '2024-02-16 22:20'),
    (27, 32, 12, 1, 3, '2024-02-16 22:20'),
    (28, 34, 10, 3, 1, '2024-02-17 03:35'),
    (29, 34, 11, 2, 2, '2024-02-17 03:35'),
    (30, 34, 16, 1, 3, '2024-02-17 03:35'),
    (31, 40, 2, 1, 1, '2024-02-17 08:50'),
    (32, 40, 7, 2, 2, '2024-02-17 08:50'),
    (33, 40, 15, 3, 3, '2024-02-17 08:50'),
    (34, 42, 9, 3, 1, '2024-02-17 14:05'),
    (35, 42, 12, 1, 2, '2024-02-17 14:05'),
    (36, 42, 18, 2, 3, '2024-02-17 14:05'),
    (37, 46, 1, 3, 1, '2024-02-17 19:20'),
    (38, 46, 6, 1, 2, '2024-02-17 19:20'),
    (39, 46, 12, 2, 3, '2024-02-17 19:20'),
    (40, 55, 3, 1, 1, '2024-02-17 00:35'),
    (41, 55, 8, 3, 2, '2024-02-17 00:35'),
    (42, 55, 13, 3, 3, '2024-02-17 00:35'),
    (43, 60, 7, 2, 1, '2024-02-17 05:50'),
    (44, 60, 12, 1, 2, '2024-02-17 05:50'),
    (45, 60, 15, 2, 3, '2024-02-17 05:50'),
    (46, 61, 4, 1, 1, '2024-02-17 11:05'),
    (47, 61, 6, 3, 2, '2024-02-17 11:05'),
    (48, 61, 12, 1, 3, '2024-02-17 11:05'),
    (49, 64, 1, 3, 1, '2024-02-17 16:20'),
    (50, 64, 4, 2, 2, '2024-02-17 16:20'),
    (51, 64, 7, 1, 3, '2024-02-17 16:20'),
    (52, 73, 3, 2, 1, '2024-03-03 13:20'),
    (53, 73, 6, 3, 2, '2024-03-03 13:20'),
    (54, 73, 18, 3, 3, '2024-03-03 13:20'),
    (55, 75, 1, 1, 1, '2024-03-05 18:35'),
    (56, 75, 6, 2, 2, '2024-03-05 18:35'),
    (57, 75, 14, 1, 3, '2024-03-05 18:35'),
    (58, 79, 9, 3, 1, '2024-03-10 03:50'),
    (59, 79, 11, 2, 2, '2024-03-10 03:50'),
    (60, 79, 14, 1, 3, '2024-03-10 03:50');
'''

# Execute the SQL command
cursor.execute(Student_Residence_Option)

Rental_Agent = '''
INSERT INTO S.Rental_Agent (rental_agent_id, rental_agent_first_name, rental_agent_last_name, email, phone_number)
VALUES 
    (1, 'Josefa', 'Tulk', 'jtulk0@gmail.com', '07812 345678'),
    (2, 'Georgeta', 'Heaker', 'gheaker1@gmail.com', '07700 123456'),
    (3, 'Roxy', 'Radbourn', 'rradbourn2@gmail.com', '07999 876543'),
    (4, 'Marlyn', 'Ellicott', 'mellicott3@gmail.com', '07555 987654'),
    (5, 'Shaughn', 'Sargeaunt', 'ssargeaunt4@gmail.com', '07777 456789'),
    (6, 'Suzie', 'Dowyer', 'sdowyer5@gmail.com', '07988 234567'),
    (7, 'Noach', 'Demare', 'ndemare6@gmail.com', '07654 321098'),
    (8, 'Tiffanie', 'Winder', 'twinder7@gmail.com', '07890 567890'),
    (9, 'Pepita', 'Donohue', 'podonohue8@gmail.com', '07722 334455'),
    (10, 'Flemming', 'Moquin', 'fmoquin9@gmail.com', '07911 223344'),
    (11, 'Willyt', 'Aldren', 'waldrena@gmail.com', '07456 789012'),
    (12, 'Baxter', 'Lancastle', 'blancastleb@gmail.com', '07577 890123');
'''

# Execute the SQL command
cursor.execute(Rental_Agent)

Student_Contract = '''
INSERT INTO S.Student_Contract (student_contract_id, rental_agent_id, student_id, room_id, offer_paid_on, arrival_date, departure_date)
VALUES 
    (1, 1, 1, 1, '2024-02-25 11:20', '2024-09-27 00:00', '2024-10-18 00:00'),
    (2, 1, 3, 8, '2024-02-25 16:35', '2024-09-29 00:00', '2024-10-18 00:00'),
    (3, 2, 9, 13, '2024-02-25 21:50', '2024-09-25 00:00', '2024-10-18 00:00'),
    (4, 2, 14, 23, '2024-02-26 03:05', '2024-09-30 00:00', '2024-10-18 00:00'),
    (5, 2, 20, 38, '2024-02-26 08:20', '2024-09-26 00:00', '2024-10-25 00:00'),
    (6, 4, 28, 21, '2024-02-26 18:50', '2024-09-28 00:00', '2024-10-18 00:00'),
    (7, 4, 30, 7, '2024-02-27 00:05', '2024-09-30 00:00', '2024-10-18 00:00'),
    (8, 5, 34, 25, '2024-02-27 14:50', '2024-09-25 00:00', '2024-10-25 00:00'),
    (9, 8, 46, 2, '2024-02-27 05:35', '2024-09-26 00:00', '2024-10-18 00:00'),
    (10, 10, 55, 5, '2024-02-27 10:50', '2024-09-28 00:00', '2024-10-18 00:00'),
    (11, 10, 60, 33, '2024-02-27 16:05', '2024-09-25 00:00', '2024-10-18 00:00'),
    (12, 11, 61, 6, '2024-02-27 21:20', '2024-09-27 00:00', '2024-10-18 00:00'),
    (13, 11, 64, 10, '2024-02-28 02:35', '2024-09-29 00:00', '2024-10-25 00:00'),
    (14, 11, 73, 47, '2024-03-17 23:20', '2024-09-28 00:00', '2024-10-25 00:00'),
    (15, 12, 79, 17, '2024-03-24 15:50', '2024-09-30 00:00', '2024-10-18 00:00');
'''

# Execute the SQL command
cursor.execute(Student_Contract)

# Use commit to get it to finish 
cnxn.commit()

# Now call all the data from the new table

# tableData = 'SELECT * FROM S.Student;'

# print('Now getting all the rows \n')

# with cursor.execute(tableData):
    # row = cursor.fetchone()
    # while row:
        # print(str(row[0]) + ' '+str(row[1]))
        # row = cursor.fetchone()
