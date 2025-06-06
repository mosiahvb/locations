import actions

# actions.add_item('6102','1-A-1')

data = [
    ('22-4-001BKS', '5-A-1'),
    ('22-4-001BLS', '5-A-1'),
    ('22-4-001CLS', '5-A-2'),
    ('22-4-001GDS', '5-A-2'),
    ('22-4-001ORS', '5-A-3'),
    ('22-4-001RDS', '5-A-3'),
    ('22-4-002BKS', '5-A-4'),
    ('22-4-002CLS', '5-A-4'),
    ('22-4-002GDS', '5-A-5'),
    ('22-4-005BKS', '5-A-5'),
    ('22-4-005BLS', '5-A-6'),
    ('22-4-005CLS', '5-A-6'),
    ('22-4-005GDS', '5-A-7'),
    ('22-4-005ORS', '5-A-7'),
    ('22-4-005RDS', '5-A-8'),
    ('22-4-007BKS', '5-A-8'),
    ('22-4-007BLS', '5-A-9'),
    ('22-4-007GDS', '5-A-9'),
    ('22-4-007PRS', '5-A-10'),
    ('22-4-009BKS', '5-A-10'),
    ('22-4-009CLS', '5-A-11'),
    ('22-4-014BKS', '5-A-11'),
    ('22-4-014BLS', '5-A-12'),
    ('22-4-014CLS', '5-A-12'),
    ('22-4-014GDS', '5-A-13'),
    ('22-4-014RDS', '5-A-13'),
    ('22-4-016BKS', '5-A-14'),
    ('22-4-016BLS', '5-A-14'),
    ('22-4-016CLS', '5-A-15'),
    ('22-4-016GDS', '5-A-15'),
    ('22-4-016ORS', '5-A-16'),
    ('22-4-016RDS', '5-A-16'),
    ('22-4-018BKS', '5-A-17'),
    ('22-4-018BLS', '5-A-17'),
    ('22-4-018CLS', '5-A-18'),
    ('22-4-018GDS', '5-A-18'),
    ('22-4-018ORS', '5-A-19'),
    ('22-4-018RDS', '5-A-19'),
    ('22-4-020BKS', '5-A-20'),
    ('22-4-020BLS', '5-A-20'),
    ('22-4-020CLS', '5-A-21'),
    ('22-4-020RDS', '5-A-21'),
    ('22-4-022-BKS', '5-A-22'),
    ('22-4-022-BLS', '5-A-22'),
    ('22-4-022-CLS', '5-A-23'),
    ('22-4-022-GDS', '5-A-23'),
    ('22-4-022-ORS', '5-A-24'),
    ('22-4-022-RDS', '5-A-24'),
    ('22-4-024BKS', '5-A-25'),
    ('22-4-024BLS', '5-A-25'),
    ('22-4-024CLS', '5-A-26'),
    ('22-4-024GDS', '5-A-26'),
    ('22-4-024ORS', '5-A-27'),
    ('22-4-024RDS', '5-A-27'),
    ('22-4-026-BKS', '5-A-28'),
    ('22-4-026-BLS', '5-A-28'),
    ('22-4-026-CLS', '5-A-29'),
    ('22-4-026-GDS', '5-A-29'),
    ('22-4-026-ORS', '5-A-30'),
    ('22-4-026-PRS', '5-A-30'),
    ('22-4-026-RDS', '5-A-31'),
    ('22-4-027-BKS', '5-A-31'),
    ('22-4-027-BLS', '5-A-32'),
    ('22-4-027-CLS', '5-A-32'),
    ('22-4-027-GDS', '5-A-33'),
    ('22-4-027-ORS', '5-A-33'),
    ('22-4-027-RDS', '5-A-34'),
    ('22-3-ADVBKS', '5-A-34'),
    ('22-3-ADVBLS', '5-A-35'),
    ('22-3-ADVCLS', '5-A-35'),
    ('22-3-ADVORS', '5-A-36'),
    ('22-3-ADVRDS', '5-A-36'),
    ('22-ADV-102BKS', '5-A-37'),
    ('22-ADV-102CLS', '5-A-37'),
    ('22-ADV-102RDS', '5-A-38'),
    ('22-ADV-106BKS', '5-A-38'),
    ('22-ADV-106BLS', '5-A-39'),
    ('22-ADV-106CLS', '5-A-39'),
    ('22-ADV-106ORS', '5-A-40'),
    ('22-ADV-111BKS', '5-A-40'),
    ('22-ADV-016BKS', '5-A-41'),
    ('22-ADV-016BLS', '5-A-41'),
    ('22-ADV-016CLS', '5-A-42'),
    ('22-ADV-016GDS', '5-A-42'),
    ('22-ADV-016ORS', '5-A-43'),
    ('22-ADV-016RDS', '5-A-43'),
    ('22-3-SA1BKS', '5-A-44'),
    ('22-3-SA1BLS', '5-A-44'),
    ('22-3-SA1CLS', '5-A-45'),
    ('22-3-SA1ORS', '5-A-45'),
    ('22-3-SA1RDS', '5-A-46'),
    ('22-3-SA2BKS', '5-A-46'),
    ('22-3-SA2BLS', '5-A-47'),
    ('22-3-SA2CLS', '5-A-47'),
    ('22-3-SA2ORS', '5-A-48'),
    ('22-3-SA2RDS', '5-A-48'),
    ('22-EXT-001BKS', '5-B-1'),
    ('22-EXT-001BLS', '5-B-1'),
    ('22-EXT-001CLS', '5-B-2'),
    ('22-EXT-001GDS', '5-B-2'),
    ('22-EXT-001ORS', '5-B-3'),
    ('22-EXT-002BKS', '5-B-3'),
    ('22-EXT-002CLS', '5-B-4'),
    ('22-EXT-002GDS', '5-B-4'),
    ('22-3-SABKS', '5-B-5'),
    ('22-3-SABLS', '5-B-5'),
    ('22-5-003', '5-B-6'),
    ('22-4-006BKS', '5-B-7'),
    ('22-4-006BLS', '5-B-7'),
    ('22-4-006CLS', '5-B-8'),
    ('22-4-006GDS', '5-B-8'),
    ('22-4-006ORS', '5-B-9'),
    ('22-4-006RDS', '5-B-9'),
    ('22-6-003-BKS', '5-B-10'),
    ('22-6-003-BLS', '5-B-10'),
    ('22-3-SACLS', '5-B-11'),
    ('22-3-SAORS', '5-B-11'),
    ('22-5-004', '5-B-12'),
    ('22-EXT-012BKS', '5-B-13'),
    ('22-EXT-013BLS', '5-B-13'),
    ('22-EXT-013BKS', '5-B-14'),
    ('22-EXT-013CLS', '5-B-14'),
    ('22-EXT-013GDS', '5-B-15'),
    ('22-EXT-013RDS', '5-B-15'),
    ('22-6-003-CLS', '5-B-16'),
    ('22-6-003-GDS', '5-B-16'),
    ('22-3-SARDS', '5-B-17'),
    ('22-SDV-016 BKS', '5-B-17'),
    ('22-5-005', '5-B-18'),
    ('22-4-017BKS', '5-B-19'),
    ('22-4-017BLS', '5-B-19'),
    ('22-4-017CLS', '5-B-20'),
    ('22-4-017GDS', '5-B-20'),
    ('22-4-017ORS', '5-B-21'),
    ('22-4-017RDS', '5-B-21'),
    ('22-4-019BKS', '5-B-22'),
    ('22-4-019BLS', '5-B-22'),
    ('22-SDV-016BLS', '5-B-23'),
    ('22-SDV-016CLS', '5-B-23'),
    ('22-5-005', '5-B-24'),
    ('22-4-019CLS', '5-B-25'),
    ('22-4-019GDS', '5-B-25'),
    ('22-4-019ORS', '5-B-26'),
    ('22-4-019RDS', '5-B-26'),
    ('22-4-021BKS', '5-B-27'),
    ('22-4-021BLS', '5-B-27'),
    ('22-4-021CLS', '5-B-28'),
    ('22-4-023BKS', '5-B-28'),
    ('22-SDV-016GDS', '5-B-29'),
    ('22-SDV-016ORS', '5-B-29'),
    ('22-5-007', '5-B-30'),
    ('22-4-023BLS', '5-B-31'),
    ('22-4-023CLS', '5-B-31'),
    ('22-4-023GDS', '5-B-32'),
    ('22-4-023ORS', '5-B-32'),
    ('22-4-023RDS', '5-B-33'),
    ('22-4-025BKS', '5-B-33'),
    ('22-4-025BLS', '5-B-34'),
    ('22-4-025CLS', '5-B-34'),
    ('22-SDV-016RDS', '5-B-35'),
    ('22-4-216BKS', '5-B-35'),
    ('22-5-007', '5-B-36'),
    ('22-4-025GDS', '5-B-37'),
    ('22-4-025ORS', '5-B-37'),
    ('22-4-025RDS', '5-B-38'),
    ('22-4-028-BKS', '5-B-38'),
    ('22-4-028-BLS', '5-B-39'),
    ('22-4-028-CLS', '5-B-39'),
    ('22-4-028-GDS', '5-B-40'),
    ('22-4-028-ORS', '5-B-40'),
    ('22-4-028-RDS', '5-B-41'),
    ('22-4-218BKS', '5-B-41'),
    ('22-5-007', '5-B-42'),
    ('22-5-002', '5-B-43'),
    ('22-4-116BKS', '5-B-43'),
    ('22-4-118BKS', '5-B-44'),
    ('22-ADV-020-BKS', '5-B-44'),
    ('22-ADV-020-BLS', '5-B-45'),
    ('22-ADV-020-CLS', '5-B-45'),
    ('22-SDV-020-BKS', '5-B-46'),
    ('22-SDV-020-BLS', '5-B-46'),
    ('22-SDV-020-CLS', '5-B-47'),
    ('22-6-003-ORS', '5-B-47'),
    ('22-6-003-RDS', '5-B-48'),
    ('22-5-009', '5-B-48'),
    ('22-6-004-BKS', '4-A-1'),
    ('22-6-004-BLS', '4-A-1'),
    ('22-6-004-CLS', '4-A-2'),
    ('22-6-004-GDS', '4-A-2'),
    ('22-6-004-ORS', '4-A-3'),
    ('22-6-004-RDS', '4-A-3'),
    ('22-6-001-BKS', '4-A-7'),
    ('22-6-001-CLS', '4-A-7'),
    ('22-6-001-RDS', '4-A-8'),
    ('ASS-DM-0201', '6-A-1'), ('22-14-0001', '6-A-1'), ('22-12-4001.5IN', '6-A-2'), 
    ('22-12-4002.0IN', '6-A-2'), ('22-12-4002.5IN', '6-A-2'), ('V2-TC-063', '6-A-3'), 
    ('V1-TC-003', '6-A-3'), ('ASS-DM-0206', '6-A-4'), ('22-14-0002', '6-A-4'), 
    ('22-12-525', '6-A-5'), ('V2-TC-065', '6-A-5'), ('V1-TC-004', '6-A-6'), 
    ('ASS-DM-0207', '6-A-6'), ('ASS-DM-0106', '6-A-7'), ('22-13-090', '6-A-7'), 
    ('V2-TC-904', '6-A-8'), ('V1-TC-065', '6-A-8'), ('ASS-DM-0301', '6-A-9'), 
    ('22-1-120', '6-A-9'), ('V2-TC-905', '6-A-10'), ('V1-TC-904', '6-A-10'), 
    ('ASS-DM-0801', '6-A-11'), ('ASS-DM-0108', '6-A-11'), ('ASS-FC-0101', '6-A-12'), 
    ('ASS-DM-0109', '6-A-12'), ('22-13-107', '6-A-13'), ('V3-TC-040', '6-A-13'), 
    ('V1-TC-905', '6-A-14'), ('V3-TC-033', '6-A-14'), ('V1-TC-960', '6-A-15'), 
    ('V2-TC-003', '6-A-15'), ('V2-TC-004', '6-A-16'), ('V3-TC-041', '6-A-16'), 
    ('ASS-DM-0111', '6-A-17'), ('22-12-325', '6-A-17'), ('ASS-DM-0113', '6-A-18'), 
    ('ASS-FC-0112', '6-A-18'), ('ASS-FC-0105', '6-A-19'), ('ASS-DM-0107', '6-A-20'), 
    ('ASV-LM-0817', '6-A-20'), ('22-1-195P', '6-A-21'), ('22-1-195P', '6-A-22'), 
    ('22-V3-040', '6-A-23'), ('22-V3-040', '6-A-24'), ('22-V3-033', '6-A-25'), 
    ('22-1-195PBLK', '6-A-26'), ('22-1-195PBLK', '6-A-27'), ('22-1-195R', '6-A-28'), 
    ('22-1-195L', '6-A-29'), ('22-1-195RBLK', '6-A-30'), ('22-1-195LBLK', '6-A-31'), 
    ('22-V2-904', '6-A-32'), ('22-V1-905', '6-A-33'), ('22-V2-063', '6-A-34'), 
    ('22-V1-960', '6-A-35'), ('22-V1-904', '6-A-36'), ('S7-CL-001', '6-B-1'), 
    ('S7-CL-002', '6-B-2'), ('S7-CL-006', '6-B-3'), ('S7-CL-006-1', '6-B-4'), 
    ('S7-CL-008', '6-B-5'), ('S7-CL-008', '6-B-6'), ('S7-CL-007', '6-B-7'), 
    ('S7-CL-009', '6-B-8'), ('S7-LT-022', '6-B-9'), ('S7-CL-010', '6-B-10'), 
    ('S7-CL-008-1', '6-B-11'), ('S7-DC-001', '6-B-12'), ('S7-DC-002', '6-B-13'), 
    ('S7-DC-004', '6-B-14'), ('S7-AC-003-BLK', '6-B-15'), ('S7-AC-003-RM', '6-B-16'), 
    ('S7-AC-003SH-BLK', '6-B-17'), ('S7-AC-003SH-RM', '6-B-18'), ('S7-AC-002-BK', '6-B-19'), 
    ('S7-AC-002-RM', '6-B-20'), ('S7-AC-001-BLK', '6-B-21'), ('S7-AC-001-RM', '6-B-22'), 
    ('44-LT-012', '6-B-23'), ('S7-MR-007', '6-B-23'), ('S7-CM-001 LG', '6-B-24'), 
    ('S7-CM-001RM', '6-B-24'), ('S7-MR-001', '6-B-25'), ('S7-KT-003', '6-B-25'), 
    ('S7-KT-004', '6-B-26'), ('S7-KT-008', '6-B-26'), ('S7-KT-001', '6-B-27'), 
    ('S7-KT-002', '6-B-27'), ('S7-KT-005', '6-B-27'), ('S7-CC-031', '6-B-28'), 
    ('44-ML-006', '6-B-28'), ('S7-CC-039', '6-B-29'), ('S7-CC-034', '6-B-29'), 
    ('S7-CC-013', '6-B-30'), ('S7-CC-016', '6-B-30'), ('44-ML-007', '6-B-31'), 
    ('44-LT-011', '6-B-31'), ('S7-LT-003', '6-B-32'), ('S7-CC-042', '6-B-32'), 
    ('S7-RN-002', '6-B-33'), ('S7-KT-009', '6-B-33'), ('S7-KT-007', '6-B-34'),
    ('PMB-01-1001', '3-A-1'),
    ('PMB-01-1002', '3-A-2'),
    ('PMB-01-1003', '3-A-3'),
    ('PMB-01-1004', '3-A-4'),
    ('PMB-01-1005', '3-A-5'),
    ('PMB-01-1006', '3-A-6'),
    ('PMB-01-1007', '3-A-7'),
    ('PMB-01-1008', '3-A-8'),
    ('PMB-01-1009', '3-A-9'),
    ('PMB-01-1010', '3-A-10'),
    ('PMB-01-1011', '3-A-11'),
    ('PMB-01-1012', '3-A-12'),
    ('PMB-01-1014', '3-A-13'),
    ('PMB-01-1015', '3-A-14'),
    ('PMB-01-1016', '3-A-15'),
    ('PMB-01-1016', '3-A-16'),
    ('PMB-01-2001', '3-A-17'),
    ('PMB-01-2002', '3-A-18'),
    ('PMB-01-2005', '3-A-19'),
    ('PMB-01-2007', '3-A-20'),
    ('PMB-01-2007', '3-A-21'),
    ('PMB-01-2007', '3-A-22'),
    ('PMB-01-2008', '3-A-23'),
    ('PMB-01-2009', '3-A-24'),
    ('PMB-01-2010', '3-A-25'),
    ('PMB-01-2010', '3-A-26'),
    ('PMB-01-2010', '3-A-27'),
    ('PMB-01-2011', '3-A-28'),
    ('PMB-01-3001', '3-A-29'),
    ('PMB-01-3002', '3-A-30'),
    ('PMB-01-3003', '3-A-31'),
    ('PMB-01-3004', '3-A-32'),
    ('PMB-01-3005', '3-A-33'),
    ('PMB-01-3006', '3-A-34'),
    ('PMB-01-3008', '3-A-35'),
    ('PMB-01-3008', '3-A-36'),
    ('PMB-01-3009', '3-A-37'),
    ('PMB-01-3010', '3-B-1'),
    ('PMB-01-3010', '3-B-2'),
    ('PMB-01-3010', '3-B-3'),
    ('PMB-01-3010', '3-B-4'),
    ('PMB-01-3010', '3-B-5'),
    ('PMB-01-3012', '3-B-6'),
    ('PMB-01-3013', '3-B-7'),
    ('PMB-01-3013', '3-B-8'),
    ('PMB-01-3014', '3-B-9'),
    ('PMB-01-3014', '3-B-10'),
    ('PMB-01-3015', '3-B-11'),
    ('PMB-01-3015', '3-B-12'),
    ('PMB-01-3015', '3-B-13'),
    ('PMB-01-3015', '3-B-14'),
    ('PMB-01-3015', '3-B-15'),
    ('PMB-01-3015', '3-B-16'),
    ('PMB-01-3015', '3-B-17'),
    ('PMB-01-3015', '3-B-18'),
    ('PMB-01-3016', '3-B-19'),
    ('PMB-01-3017', '3-B-20'),
    ('PMB-01-3018', '3-B-21'),
    ('PMB-01-3019', '3-B-22'),
    ('PMB-01-4001', '3-B-23'),
    ('PMB-01-4002', '3-B-24'),
    ('PMB-01-4005', '3-B-25'),
    ('PMB-01-4008', '3-B-26'),
    ('PMB-01-4011', '3-B-27'),
    ('PMB-01-5001', '3-B-28'),
    ('PMB-01-5001', '3-B-29'),
    ('PMB-01-5002', '3-B-30'),
    ('PMB-01-5003', '3-B-31'),
    ('PMB-01-5003', '3-B-32'),
    ('PMB-01-5003', '3-B-33'),
    ('PMB-01-5004', '3-B-34'),
    ('PMB-01-5005', '3-B-35'),
    ('PMB-01-5006', '3-B-36'),
    ('PMB-01-5007', '3-B-37'),
    ('PMB-01-5007', '3-B-38'),
    ('PMB-01-5007', '3-B-39'),
    ('PMB-01-5008', '3-B-40'),
    ('PMB-01-5009', '3-B-41'),
    ('PMB-01-5010', '3-B-42'),
    ('PMB-01-6002', '3-B-43'),
    ('PMB-01-7002', '3-B-44'),
    ('PMB-01-7003', '3-B-45'),
    ('PMB-01-7004', '3-B-46')
]


actions.show_all()

print('MENU!')
print()
print('1. Show all: ')
print('2. Look up location: ')
print('3. Add a part and location')
print('4. Change a location')
print('5. Delete all')
print('6. Mass Add')
print()

choice = int(input('Please pick a number 1-3: '))

#shows what in the data base
if choice == 1:
    actions.show_all()

# looks up where your designated parts location is
elif choice == 2:
    print('What part number are you looking for?')
    part = input(': ')
    actions.look_up(part)

# adds a part to the database
elif choice == 3:
    print('Add your part name')
    part_name = input(': ')
    print('Add your part Location')
    part_location = input(': ')

    actions.add_item(part_name, part_location)
    print('I part and location successfully updated!')

elif choice == 4:
    actions.change_location()

elif choice == 5:
    actions.deleteall()

elif choice == 6:
    actions.mass_insert(data)

else:
    print('invalid entry!')
