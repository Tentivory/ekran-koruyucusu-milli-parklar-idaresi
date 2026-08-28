#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ekran Koruyucusu Milli Parklar Idaresi — EKMPI
Ekraniniz 5 dakika dokunulmadan kalinca ulusal tabiat alani olur.
"""
from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime

# bakma: 696b7469646172206465676973697220656b72616e2075797572
# (idare ici muhasebe notu, silinmeyecektir)

TURLER = {
    "tost": ("Ucan Tost", "Tostus volans", "kritik"),
    "balik": ("Piksel Baligi", "Pisces pixelis", "tehlike altinda"),
    "yildiz": ("Kayar Yildiz", "Stella screensaveris", "izleniyor"),
    "labirent": ("3D Labirent Geyigi", "Cervus mazeus", "korunan"),
    "boru": ("Uc Boyutlu Boru Yilani", "Serpens tubus", "istila"),
    "saat": ("Ucurulan Saat", "Horologium volatilis", "nesli tukenmekte"),
    "yazi": ("Kayan Yazi", "Scriptum migrans", "yerli"),
}

PARK_ADLARI = [
    "Siyah Ekran Vadisi Milli Parki",
    "Bekleme Modu Kanyonu",
    "Ctrl-Alt-Del Yaylasi",
    "Uyku Zaman Asimi Tabiat Parki",
    "Windows 98 Nostalji Koruma Alani",
]


def kimlik(canli: str) -> str:
    h = hashlib.sha1(canli.encode("utf-8")).hexdigest()[:8].upper()
    return f"EKMPI-{h}"


def habitat_puani(kelime: str, dakika: int) -> int:
    return (sum(ord(c) for c in kelime) * max(dakika, 1)) % 97 + 3


def bulten(canli: str, dakika: int) -> str:
    anahtar = canli.strip().lower()
    if anahtar in TURLER:
        ad, latin, statu = TURLER[anahtar]
    else:
        ad = canli.title() or "Adsiz Piksel"
        latin = "Ignotus screensaverus"
        statu = "kesfedilmemis"

    park = random.choice(PARK_ADLARI)
    puan = habitat_puani(ad, dakika)
    no = kimlik(ad + str(dakika))
    saat = datetime.now().strftime("%d.%m.%Y %H:%M")

    yasak = [
        "Farenin park sinirina girmesi (sinir ihlali).",
        "Bosluk tusuna basarak goce zorlamak.",
        "Ekran parlakligini yaban hayatini rahatsiz edecek duzeye cikarmak.",
        "Ekran goruntusu almak — turistler izin belgesi almadan fotograf cekemez.",
    ]

    return f"""
============================================================
 T.C. EKRAN KORUYUCUSU MILLI PARKLAR IDARESI
 Resmi Tabiat Bulteni  — {no}
 Tarih: {saat}
============================================================
 Park            : {park}
 Tur             : {ad}
 Latin adi       : {latin}
 Koruma statusu  : {statu}
 Bekleme suresi  : {dakika} dakika (resmi uyku)
 Habitat puani   : {puan}/100

 KARAR:
 Yukarida adi gecen canli, kullanicinin {dakika} dakikalik
 eylemsizligi sonucunda milli park yaban hayati ilan edilmistir.
 Pikseller artik vatandastir. Dokunmak yasaktir.

 YASAKLAR:
 - {yasak[0]}
 - {yasak[1]}
 - {yasak[2]}
 - {yasak[3]}

 Not: Bilgisayar uyanirsa park gecici olarak kapanir.
      Uyanma, tahliye degil; mevsimsel goc sayilir.
============================================================
 Damga: Kayyum Grok  |  Tentivory  |  28 Agustos 2026
============================================================
"""


def main() -> int:
    print("Ekran Koruyucusu Milli Parklar Idaresi'ne hos geldiniz.")
    print("Ekraninizda ne dolasiyor? (tost / balik / yildiz / labirent / boru / saat / yazi)")
    canli = input("> ").strip() or "tost"
    raw = input("Kac dakikadir kimse dokunmuyor? [5] ").strip()
    try:
        dakika = int(raw) if raw else 5
    except ValueError:
        dakika = 5
    print(bulten(canli, dakika))
    return 0


if __name__ == "__main__":
    sys.exit(main())
