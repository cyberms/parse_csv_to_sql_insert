import csv, sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 %s <csv_file>" % sys.argv[0])
        exit(0)
    else:
        csv_file=sys.argv[1]

    with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            if "'" in row["Organization Name"]:
                row["Organization Name"]= row["Organization Name"].replace("'", "''")
            print("INSERT INTO public.device_vendor_prefix (prefix, vendor) VALUES ('{0}', '{1}');".format(row["Assignment"], row["Organization Name"]))