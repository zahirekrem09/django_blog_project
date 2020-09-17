
class GenderChoices(object):
    KADIN = 0
    ERKEK = 1

    CHOICES = (
        (ERKEK, "Erkek"),
        (KADIN, "Kadın")
    )


class MartialStatusChoices(object):
    EVLI = 0
    BEKAR = 1

    CHOICES = (
        (BEKAR, "Bekar"),
        (EVLI, "Evli")
    )


class EducationalStatusChoices(object):
    ILKOKUL = 0
    ORTAOKUL = 1
    LISE = 2
    UNIVERSITE = 3
    YUKSEKLISANS_DOKTORA = 4

    CHOICES = (
        (ILKOKUL, "İlkokul"),
        (ORTAOKUL, "Ortaokul"),
        (LISE, "Lise"),
        (UNIVERSITE, "Üniversite"),
        (YUKSEKLISANS_DOKTORA, "Yüksek Lisans / Doktora"),
    )


class ProfessionChoices(object):
    OZEL_SEKTOR = 0
    OGRENCI = 1
    KAMU_CALISANI = 2
    SERBEST_MESLEK = 3
    EV_HANIMI = 4
    EMEKLI = 5
    CALISMIYORUM = 6
    CIFTCI = 7

    CHOICES = (
        (OZEL_SEKTOR, "Özel Sektör"),
        (OGRENCI, "Öğrenci"),
        (KAMU_CALISANI, "Kamu Çalışanı"),
        (SERBEST_MESLEK, "Serbest Meslek"),
        (EV_HANIMI, "Ev Hanımı"),
        (EMEKLI, "Emekli"),
        (CALISMIYORUM, "Çalışmıyorum"),
        (CIFTCI, "Çiftçi"),
    )


class CategoryChoices(object):
    CHOICES = (
        ("PYTHON", "Python"),
        ("JAVA", "Java"),
        ("JAVASCRIPT", "Javascript"),
        ("LINUX", "Linux"),
        ("CSS", "Css"),
        ("HTML", "Html"),
        ("REACT", "React"),
        ("DEVOPS", "Devops"),
    )
