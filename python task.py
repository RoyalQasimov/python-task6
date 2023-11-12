import sqlite3

conn = sqlite3.connect('banka.db')
cursor = conn.cursor()

def bakiyeyi_kontrol_et(kullanici_id):
    cursor.execute(f"SELECT bakiye FROM kullanici WHERE kullanici_id = '{kullanici_id}'")
    bakiye = cursor.fetchone()
    if bakiye:
        return bakiye[0]
    else:
        return None


def para_cek(kullanici_id, cekilen_miktar):
    cursor.execute(f"UPDATE kullanici SET bakiye = bakiye - {cekilen_miktar} WHERE kullanici_id = '{kullanici_id}'")
    conn.commit()

def para_yatir(kullanici_id, yatirilan_miktar):
    cursor.execute(f"UPDATE kullanici SET bakiye = bakiye + {yatirilan_miktar} WHERE kullanici_id = '{kullanici_id}'")
    conn.commit()

def pin_degistir(kullanici_id, yeni_pin):
    cursor.execute(f"UPDATE kullanici SET pin = '{yeni_pin}' WHERE kullanici_id = '{kullanici_id}'")
    conn.commit()

conn.close()
