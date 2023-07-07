from random import sample
import mysql.connector
from tkinter import *
import os
from tkinter import messagebox
import datetime

#PRG1100-Oblig2-AAA

def vitnemal():

    def sok_student():
        sok_student_markor=mindatabase.cursor()

        sok_studnr=sok.get()

        sok_student_markor.execute("SELECT Student.Studentnr,Eksamensresultat.Emnekode,Karakter,Emne.Emnenavn,Emne.Studiepoeng,Emne.Emnekode FROM Student,Eksamensresultat,Emne WHERE Student.Studentnr=Eksamensresultat.Studentnr AND Student.Studentnr='%s' AND Eksamensresultat.Emnekode=Emne.Emnekode ORDER BY Eksamensresultat.Emnekode"%(sok_studnr,))

        studiepoeng=0

        resultat=''
        for row in sok_student_markor:
            studnr.set(row[0])
            studpoeng.set(row[4])
            studiepoeng+=(float(row[4]))
            resultat += str(row[1]) + ' ' + ' ' + str(row[3]) + ' ' + ' ' + str(row[2]) + ' ' + ' ' + str(row[4]) + '\n'
        
        studpoeng.set(studiepoeng)
        sok_student_markor.close()

        #Lager en laber for resultatet
        lbl_res=Label(vitnemal, text=resultat, bd=2, font=('Helvetica', 10), justify='left')
        lbl_res.grid(row=2, column=0, columnspan=2, ipadx=10, ipady=10)


    vitnemal=Toplevel()
    vitnemal.title('Vitnemål')

    #Utdata
    lbl_sok=Label(vitnemal, text='Søk studentnr:')
    lbl_sok.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    lbl_studnr=Label(vitnemal, text='Studentnr:')
    lbl_studnr.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    lbl_stdpoeng=Label(vitnemal, text='Studiepoeng:')
    lbl_stdpoeng.grid(row=1, column=2, padx=5, pady=5)

    #Inndata
    sok=StringVar()
    ent_sok=Entry(vitnemal, width=10, textvariable=sok)
    ent_sok.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    studnr=StringVar()
    ent_studnr=Entry(vitnemal, width=10, state='readonly', textvariable=studnr)
    ent_studnr.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    studpoeng=StringVar()
    ent_studpoeng=Entry(vitnemal, width=4, state='readonly', textvariable=studpoeng)
    ent_studpoeng.grid(row=1, column=3, padx=5, pady=5)

    #Knapper
    btn_sok=Button(vitnemal, text='Søk:', command=sok_student)
    btn_sok.grid(row=0, column=2, padx=5, pady=5, sticky=E)

    btn_tilbake=Button(vitnemal, text='Tilbake', command=vitnemal.destroy)
    btn_tilbake.grid(row=3, column=3, padx=5, pady=5, sticky=W)

def eksamensresultat():
    def kule_punkt_7():
        def sok_emnekode():

            sok_studnr=mindatabase.cursor()
            
            studentnr=sok.get()
            
            sok_studnr.execute("SELECT Eksamensresultat.*,Emne.Studiepoeng FROM Eksamensresultat,Emne WHERE Eksamensresultat.Studentnr=%s GROUP BY Eksamensresultat.Dato"%(studentnr,))
            
            studiepoeng=0

            resultat=''
            for row in sok_studnr:
                studnr.set(row[0])
                studpoeng.set(row[4])
                studiepoeng+=(float(row[4]))
                resultat += str(row[0]) + ' ' + ' ' + str(row[1]) + ' ' + ' ' + str(row[2]) + ' ' + ' ' + str(row[3]) + ' ' + ' ' + str(row[4]) + '\n'
            
            studpoeng.set(studiepoeng)
            sok_studnr.close()

            #Lager en laber for resultatet
            lbl_res=Label(kp_7, text=resultat, bd=2, font=('Helvetica', 10), justify='left')
            lbl_res.grid(row=2, column=0, columnspan=2, ipadx=10, ipady=10)

        kp_7=Toplevel()
        kp_7.title('Utksrift')

        #Utdata
        lbl_sok=Label(kp_7, text='Søk studentnr:')
        lbl_sok.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_studnr=Label(kp_7, text='Studentnr:')
        lbl_studnr.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_studpoeng=Label(kp_7, text='Studiepoeng:')
        lbl_studpoeng.grid(row=1, column=2, padx=10, pady=10, sticky=E)

        #Inndata
        sok=StringVar()
        ent_sok=Entry(kp_7, width=10, textvariable=sok)
        ent_sok.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        studnr=StringVar()
        ent_studnr=Entry(kp_7, width=10, state='readonly', textvariable=studnr)
        ent_studnr.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        studpoeng=StringVar()
        ent_studpoeng=Entry(kp_7, width=4, state='readonly', textvariable=studpoeng)
        ent_studpoeng.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        #Knapper
        btn_sok=Button(kp_7, text='Søk:', command=sok_emnekode)
        btn_sok.grid(row=0, column=2, padx=5, pady=5, sticky=E)

        btn_tilbake=Button(kp_7, text='Tilbake', command=kp_7.destroy)
        btn_tilbake.grid(row=3, column=3, padx=5, pady=5, sticky=W)

    def kar_stat():
        def sok_emnekode():

            sok_emne_kode=mindatabase.cursor()

            sok_emnekode=sok.get()

            sok_emne_kode.execute("SELECT Eksamensresultat.Emnekode,Karakter, COUNT(Karakter) AS AntallKarakterer FROM Eksamensresultat WHERE Eksamensresultat.Emnekode='%s' GROUP BY Eksamensresultat.Karakter"%(sok_emnekode,))

            resultat=''

            for row in sok_emne_kode:
                emnekode.set(row[0])
                resultat += str(row[0]) + ' ' + ' ' + str(row[1]) + ' ' + ' ' + str(row[2]) +  '\n'
            sok_emne_kode.close()

            #Lager en laber for resultatet
            lbl_res=Label(karakter, text=resultat, bd=2, font=('Helvetica', 10), justify='left')
            lbl_res.grid(row=2, column=0, columnspan=2, ipadx=10, ipady=10)

        karakter=Toplevel()
        karakter.title('Karakterfordeling')

        #Utdata
        lbl_sok=Label(karakter, text='Søk emnekode:')
        lbl_sok.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_emnekode=Label(karakter, text='Emnekode:')
        lbl_emnekode.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        #Inndata
        sok=StringVar()
        ent_sok=Entry(karakter, width=8, textvariable=sok)
        ent_sok.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        emnekode=StringVar()
        ent_emnekode=Entry(karakter, width=8, state='readonly', textvariable=emnekode)
        ent_emnekode.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #Knapper
        btn_sok=Button(karakter, text='Søk', command=sok_emnekode)
        btn_sok.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        btn_tilbake=Button(karakter, text='Tilbake', command=karakter.destroy)
        btn_tilbake.grid(row=3, column=3, padx=5, pady=5, sticky=W)

    def kar_liste():
        def sok_emnekode():

            soke_markor=mindatabase.cursor()

            emnekode=sok.get()

            soke_markor.execute("SELECT Eksamensresultat.*,Student.Studentnr,Emne.Emnekode FROM Eksamensresultat,Student,Emne WHERE Student.Studentnr=Eksamensresultat.Studentnr AND Eksamensresultat.Emnekode=Emne.Emnekode ORDER BY Eksamensresultat.Studentnr")

            resultat=''
            for row in soke_markor:
                if emnekode==row[1]:
                    resultat += str(row[0]) + ' ' + ' ' + str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3]) + '\n'
            soke_markor.close()

            #Lager en laber for resultatet
            lbl_res=Label(vindu, text=resultat, bd=2, font=('Helvetica', 10), justify='left')
            lbl_res.grid(row=2, column=0, columnspan=2, ipadx=10, ipady=10)

        vindu=Toplevel()
        vindu.title('Karakterliste')

        #Utdata
        lbl_sok=Label(vindu, text='Søk emnekode:')
        lbl_sok.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        #Inndata
        sok=StringVar()
        ent_sok=Entry(vindu, width=10, textvariable=sok)
        ent_sok.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #Knapp
        btn_sok=Button(vindu, text='Søk', command=sok_emnekode)
        btn_sok.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        btn_tilbake=Button(vindu, text='Tilbake', command=vindu.destroy)
        btn_tilbake.grid(row=3, column=3, padx=5, pady=5, sticky=W)

    def reg_samlet():
        def hent_emnekoder(event):

            valgt_emnekode=lst_emnekoder.get(lst_emnekoder.curselection())

            emnekode_eksamen_markor=mindatabase.cursor()

            emnekode_eksamen_markor.execute("SELECT * FROM Eksamen ORDER BY Emnekode")

            #Finne riktig emnekode
            for row in emnekode_eksamen_markor:
                if valgt_emnekode==row[0]:
                    emnekode.set(row[0])
                    dato.set(row[1])
            emnekode_eksamen_markor.close()

        def hent_studenter(event):
            valgt=lst_studenter.get(lst_studenter.curselection())

            studentogkarakter_markor=mindatabase.cursor()
            studentogkarakter_markor.execute("SELECT * FROM Student")

            #Finne riktig studentnr
            for row in studentogkarakter_markor:
                if valgt==row[0]:
                    studnr.set(row[0])
            studentogkarakter_markor.close()

        def reg_ny_kar():
            ny_kar_markor=mindatabase.cursor()

            studentnummer=studnr.get()
            emne_kode=emnekode.get()
            dato_hent=dato.get()
            ny_kar=ny_karakter.get()

            registrer_ny_karakter=("INSERT INTO Eksamensresultat"
                                    "(Studentnr,Emnekode,Dato,Karakter)"
                                    "VALUES(%s,%s,%s,%s)")
            
            datany_karakter=(studentnummer,emne_kode,dato_hent,ny_kar)
            ny_kar_markor.execute(registrer_ny_karakter,datany_karakter,)

            mindatabase.commit()
            ny_kar_markor.close()

            ent_studentnr.delete(0, END)
            ent_emnekode.delete(0, END)
            ent_dato.delete(0, END)
            ent_ny_karakter.delete(0, END)

        #Oppretter ny markør for listeboksen
        student_markor=mindatabase.cursor()

        student_markor.execute("SELECT * FROM Student")

        studenter=[]
        for row in student_markor:
            studenter +=[row[0]]

        #Oppretter ny markør for listeboks_2
        emnekode_markor=mindatabase.cursor()

        emnekode_markor.execute("SELECT * FROM Eksamen")

        emnekoder=[]
        for row in emnekode_markor:
            emnekoder +=[row[0]]

        #Oppretter nytt vindu for å registrere karakterer
        reg_karakter=Toplevel()
        reg_karakter.title('Samlet karakterregistrering')

        #Scrollbar
        y_scroll=Scrollbar(reg_karakter,orient=VERTICAL)
        y_scroll.grid(row=0, column=2, rowspan=10, padx=(0,50), pady=5, sticky=NS)

        innhold_i_lst_studenter=StringVar()
        lst_studenter=Listbox(reg_karakter, width=10, height=10, listvariable=innhold_i_lst_studenter)
        lst_studenter.grid(row=0, column=1, rowspan=10, padx=(50,0), pady=5, sticky=E)
        innhold_i_lst_studenter.set(tuple(studenter))
        y_scroll["command"]=lst_studenter.yview

        y_scroll_2=Scrollbar(reg_karakter,orient=VERTICAL)
        y_scroll_2.grid(row=0, column=3, rowspan=10, padx=(0,50), pady=5, sticky=NS)

        innhold_i_lst_emnekoder=StringVar()
        lst_emnekoder=Listbox(reg_karakter, width=10, height=10, listvariable=innhold_i_lst_emnekoder)
        lst_emnekoder.grid(row=0, column=2, rowspan=10, padx=(50,0), pady=5, sticky=E)
        innhold_i_lst_emnekoder.set(tuple(emnekoder))
        y_scroll_2["command"]=lst_emnekoder.yview

        #Utdata
        lbl_ny_karakter=Label(reg_karakter, text='Karakter:')
        lbl_ny_karakter.grid(row=1, column=4, padx=5, pady=5, sticky=E)

        lbl_emnekode=Label(reg_karakter, text='Emnekode:')
        lbl_emnekode.grid(row=2, column=4, padx=5, pady=5, sticky=E)

        lbl_dato=Label(reg_karakter, text='Dato:')
        lbl_dato.grid(row=3, column=4, padx=5, pady=6, sticky=E)

        lbl_studentnr=Label(reg_karakter, text='Studentnr:')
        lbl_studentnr.grid(row=4, column=4, padx=5, pady=5, sticky=E)

        #Inndata
        ny_karakter=StringVar()
        ent_ny_karakter=Entry(reg_karakter, width=2, textvariable=ny_karakter)
        ent_ny_karakter.grid(row=1, column=5, padx=5, pady=5, sticky=W)

        studnr=StringVar()
        ent_studentnr=Entry(reg_karakter, width=7, textvariable=studnr)
        ent_studentnr.grid(row=4, column=5, padx=5, pady=5, sticky=W)

        dato=StringVar()
        ent_dato=Entry(reg_karakter, width=10, textvariable=dato)
        ent_dato.grid(row=3, column=5, padx=5, pady=5, sticky=W)

        emnekode=StringVar()
        ent_emnekode=Entry(reg_karakter, width=8, textvariable=emnekode)
        ent_emnekode.grid(row=2, column=5, padx=5, pady=5, sticky=W)

        #Knapper
        btn_lagre=Button(reg_karakter, text='Lagre', command=reg_ny_kar)
        btn_lagre.grid(row=9, column=5, padx=5, pady=5, sticky=W)

        btn_tilbake=Button(reg_karakter, text='Tilbake', command=reg_karakter.destroy)
        btn_tilbake.grid(row=10, column=5, padx=5, pady=5, sticky=W)

        #Binding
        lst_studenter.bind("<<ListboxSelect>>",hent_studenter)
        lst_emnekoder.bind("<<ListboxSelect>>",hent_emnekoder)

        student_markor.close()


    #Def for å opprette nytt vindu samt flere def'er for å slette eksamensresultat
    def slette_eks_res():
        #Def for å hente informajson fra eksamensresultat
        def sok_slett():
            
            soke_markor=mindatabase.cursor()

            studentnummer=studnr_les_slett.get()
            dato_sok=sok_dato.get()
            datetime.datetime.strptime(dato_sok,"%Y-%m-%d")

            soke_markor.execute("SELECT Studentnr,Emnekode,Dato,Karakter FROM Eksamensresultat WHERE Studentnr='%s' AND Dato='%s'"%(studentnummer,dato_sok,))

            #Finner riktig studentnummer
            for row in soke_markor:
                studnr_slett.set(row[0])
                studnr_les_slett.set(row[0])
                emnekode_slett.set(row[1])
                dato_slett.set(row[2])
                karakter_slett.set(row[3])
            soke_markor.close()

        def slett_eksres():

            studentnummer=studnr_slett.get()
            emne_kode=emnekode_slett.get()
            dato=dato_slett.get()
            kar=karakter_slett.get()
            datetime.datetime.strptime(dato,"%Y-%m-%d")

            #Oppretter markør
            slett_markor=mindatabase.cursor()

            slette_eksres=("DELETE FROM Eksamensresultat WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s AND Karakter=%s")

            datany_slette=(studentnummer,emne_kode,dato,kar,)

            slett_markor.execute(slette_eksres,datany_slette)

            #Bekrefter endringer
            mindatabase.commit()

            #Stenger markøren
            slett_markor.close()

            #Stenger vindu etter fullført handling
            slett_eksamensres.destroy()

        #Oppretter nytt vindu
        slett_eksamensres=Toplevel()
        slett_eksamensres.title('Slette eksamensresultat')
        
        #Utdata
        lbl_studnr_reg=Label(slett_eksamensres, text='Søk studentnr*')
        lbl_studnr_reg.grid(row=0, column=0, padx=10, pady=10, sticky=E)

        lbl_dato_sok=Label(slett_eksamensres, text='Søk dato*')
        lbl_dato_sok.grid(row=1, column=0, padx=10, pady=10, sticky=E)

        lbl_studnr_slett=Label(slett_eksamensres, text='Studentnr:')
        lbl_studnr_slett.grid(row=3, column=0, padx=10, pady=10, sticky=E)

        lbl_emnekode_reg=Label(slett_eksamensres, text='Emnekode:')
        lbl_emnekode_reg.grid(row=4, column=0, padx=10, pady=10, sticky=E)

        lbl_dato_reg=Label(slett_eksamensres, text='Dato[YYYY-MM-DD]:')
        lbl_dato_reg.grid(row=5, column=0, padx=10, pady=10, sticky=E)

        lbl_kar_reg=Label(slett_eksamensres, text='Karakter:')
        lbl_kar_reg.grid(row=6, column=0, padx=10, pady=10, sticky=E)

        #Inndata
        studnr_les_slett=StringVar()
        ent_studnr_slett=Entry(slett_eksamensres, width=6, textvariable=studnr_les_slett)
        ent_studnr_slett.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        sok_dato=StringVar()
        ent_dato_sok=Entry(slett_eksamensres, width=10, textvariable=sok_dato)
        ent_dato_sok.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        studnr_slett=StringVar()
        ent_studnr_slett=Entry(slett_eksamensres, width=6, state='readonly', textvariable=studnr_slett)
        ent_studnr_slett.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        emnekode_slett=StringVar()
        ent_emnekode_slett=Entry(slett_eksamensres, width=8, state='readonly', textvariable=emnekode_slett)
        ent_emnekode_slett.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        dato_slett=StringVar()
        ent_dato_slett=Entry(slett_eksamensres, width=10, state='readonly', textvariable=dato_slett)
        ent_dato_slett.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        karakter_slett=StringVar()
        ent_kar_slett=Entry(slett_eksamensres, width=5, state='readonly', textvariable=karakter_slett)
        ent_kar_slett.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        #Knapper
        btn_sok=Button(slett_eksamensres, text='Søk', command=sok_slett)
        btn_sok.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        btn_lagre_slett=Button(slett_eksamensres, text='Slett resultat', command=slett_eksres)
        btn_lagre_slett.grid(row=7, column=1, columnspan=2, padx=10, pady=10, sticky=W)

        btn_tilbake_reg=Button(slett_eksamensres, text='Tilbake', command=slett_eksamensres.destroy)
        btn_tilbake_reg.grid(row=9, column=2, padx=10, pady=10, sticky=W)

    #Oppretter nytt vindu samt flere def'er for endring av eksamensresultat
    def endre_eks_res():
        #Def for å hente ut informasjon om eksamensresultat
        def sok_endre():
            soke_markor=mindatabase.cursor()

            studentnummer=studnr_les_endre.get()
            dato_sok=sok_dato.get()
            datetime.datetime.strptime(dato_sok,"%Y-%m-%d")

            soke_markor.execute("SELECT Studentnr,Emnekode,Dato,Karakter FROM Eksamensresultat WHERE Studentnr='%s' AND Dato='%s'"%(studentnummer,dato_sok,))
            
            #Finner riktig informasjon
            for row in soke_markor:
                studnr_les_endre.set(row[0])
                ny_studnr.set(row[0])
                emnekode_endre.set(row[1])
                dato_endre.set(row[2])
                karakter_endre.set(row[3])
            soke_markor.close()
            
        #Def for å endre eksamensresultat
        def endre_eksresultat():
            endre_resultat_markor=mindatabase.cursor()

            studentnr=studnr_les_endre.get()
            emnekode=emnekode_endre.get()
            dato=dato_endre.get()
            kar=karakter_endre.get()
            stud_nr=ny_studnr.get()

            endre_eksres=("UPDATE Eksamensresultat SET Studentnr=%s,Emnekode=%s,Dato=%s,Karakter=%s WHERE Studentnr=%s")

            datany_eksres=(studentnr,emnekode,dato,kar,stud_nr,)

            endre_resultat_markor.execute(endre_eksres,datany_eksres,)

            #Bekrefter endringer mot databasen
            mindatabase.commit()
            
            #Stenger vinduet for endring av resultat
            endre_resultat_markor.close()

            #Stenger vindu for endring av eksamensresultat
            endre_eksamensres.destroy()

        #Oppretter nytt vindu
        endre_eksamensres=Toplevel()
        endre_eksamensres.title('Endre eksamensresultat')

        #Utdata
        lbl_studnr_reg=Label(endre_eksamensres, text='Søk studentnr*')
        lbl_studnr_reg.grid(row=0, column=0, padx=10, pady=10, sticky=E)

        lbl_dato_sok=Label(endre_eksamensres, text='Søk dato*')
        lbl_dato_sok.grid(row=1, column=0, padx=10, pady=10, sticky=E)

        lbl_stud_nr=Label(endre_eksamensres, text='Studentnr:')
        lbl_stud_nr.grid(row=3, column=0, padx=10, pady=10, sticky=E)

        lbl_emnekode_reg=Label(endre_eksamensres, text='Emnekode:')
        lbl_emnekode_reg.grid(row=4, column=0, padx=10, pady=10, sticky=E)

        lbl_dato_reg=Label(endre_eksamensres, text='Dato[yyyy-mm-dd]:')
        lbl_dato_reg.grid(row=5, column=0, padx=10, pady=10, sticky=E)

        lbl_kar_reg=Label(endre_eksamensres, text='Karakter:')
        lbl_kar_reg.grid(row=6, column=0, padx=10, pady=10, sticky=E)

        #Inndata
        studnr_les_endre=StringVar()
        ent_studnr_reg=Entry(endre_eksamensres, width=6, textvariable=studnr_les_endre)
        ent_studnr_reg.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        sok_dato=StringVar()
        ent_dato_sok=Entry(endre_eksamensres, width=10, textvariable=sok_dato)
        ent_dato_sok.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        ny_studnr=StringVar()
        ent_stud_nr=Entry(endre_eksamensres, width=6, textvariable=ny_studnr)
        ent_stud_nr.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        emnekode_endre=StringVar()
        ent_emnekode_reg=Entry(endre_eksamensres, width=8, textvariable=emnekode_endre)
        ent_emnekode_reg.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        dato_endre=StringVar()
        ent_dato_reg=Entry(endre_eksamensres, width=10, textvariable=dato_endre)
        ent_dato_reg.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        karakter_endre=StringVar()
        ent_kar_reg=Entry(endre_eksamensres, width=5, textvariable=karakter_endre)
        ent_kar_reg.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        #Knapper
        btn_sok=Button(endre_eksamensres, text='Søk', command=sok_endre)
        btn_sok.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        btn_lagre_reg=Button(endre_eksamensres, text='Lagre', command=endre_eksresultat)
        btn_lagre_reg.grid(row=7, column=1, columnspan=2, padx=10, pady=10, sticky=W)

        btn_tilbake_reg=Button(endre_eksamensres, text='Tilbake', command=endre_eksamensres.destroy)
        btn_tilbake_reg.grid(row=8, column=2, padx=10, pady=10, sticky=W)

    #Oppretter vindu samt flere def'er for å gjennomføre registrering av eksamensresultat
    def reg_eks_res():

        #Def for å hente informasjon om studenter
        def hent_student(event):
            valgt=lst_studenter.get(lst_studenter.curselection())

            student_markor=mindatabase.cursor()
            student_markor.execute("""SELECT Studentnr FROM Student""")

            #Finner riktig studentnummer
            for row in student_markor:
                if valgt==row[0]:
                    studnr_les.set(row[0])
            student_markor.close()

        student_to_markor=mindatabase.cursor()

        student_to_markor.execute("SELECT * FROM Student")

        #Bruker resultatet
        studenter=[]
        for row in student_to_markor:
            studenter+=[row[0]]

        #Def for å registrere eksamensresultat
        def registrer_eksresultat():

            #Oppretter markør
            leggtil_res_markor=mindatabase.cursor()

            studentnr=studnr_les.get()
            emnekode=emnekode_reg.get()
            dato=dato_reg.get()
            kar=karakter.get()

            #Legger til resultat
            leggtil_res=("INSERT INTO Eksamensresultat"
                        "(Studentnr,Emnekode,Dato,Karakter)"
                        "VALUES(%s,%s,%s,%s)")

            datany_res=(studentnr,emnekode,dato,kar)
            leggtil_res_markor.execute(leggtil_res,datany_res)

            #Bekrefter endringer
            mindatabase.commit()

            #Stenger markøren
            leggtil_res_markor.close()

            #fjerner inndatafeltene
            ent_emnekode_reg.delete(0, END)
            ent_dato_reg.delete(0, END)
            ent_kar_reg.delete(0, END)

        #Oppretter Toplevel vindu for å registrere eksamen
        reg_eksamensres=Toplevel()
        reg_eksamensres.title('Registrere eksamensresultat')
        y_scroll=Scrollbar(reg_eksamensres, orient=VERTICAL)
        y_scroll.grid(row=0, column=2, rowspan=5, padx=(0,10), pady=5, sticky=NS)

        #Listeboks
        innhold_i_lst_studenter=StringVar()
        lst_studenter=Listbox(reg_eksamensres, width=25, height=10, listvariable=innhold_i_lst_studenter, yscrollcommand=y_scroll.set)
        lst_studenter.grid(row=0, column=1, rowspan=5, padx=(10,0), pady=5, sticky=E)
        innhold_i_lst_studenter.set(tuple(studenter))
        y_scroll["command"]=lst_studenter.yview

        #Utdata
        lbl_studnr_reg=Label(reg_eksamensres, text='Studentnr')
        lbl_studnr_reg.grid(row=0, column=3, padx=10, pady=10, sticky=E)

        lbl_emnekode_reg=Label(reg_eksamensres, text='Emnekode:')
        lbl_emnekode_reg.grid(row=1, column=3, padx=10, pady=10, sticky=E)

        lbl_dato_reg=Label(reg_eksamensres, text='Dato[yyyy-mm-dd]:')
        lbl_dato_reg.grid(row=2, column=3, padx=10, pady=10, sticky=E)

        lbl_kar_reg=Label(reg_eksamensres, text='Karakter:')
        lbl_kar_reg.grid(row=3, column=3, padx=10, pady=10, sticky=E)

        #Inndata
        studnr_les=StringVar()
        ent_studnr_reg=Entry(reg_eksamensres, width=6, state='readonly', textvariable=studnr_les)
        ent_studnr_reg.grid(row=0, column=4, padx=10, pady=10, sticky=W)

        emnekode_reg=StringVar()
        ent_emnekode_reg=Entry(reg_eksamensres, width=8, textvariable=emnekode_reg)
        ent_emnekode_reg.grid(row=1, column=4, padx=10, pady=10, sticky=W)

        dato_reg=StringVar()
        ent_dato_reg=Entry(reg_eksamensres, width=10, textvariable=dato_reg)
        ent_dato_reg.grid(row=2, column=4, padx=10, pady=10, sticky=W)

        karakter=StringVar()
        ent_kar_reg=Entry(reg_eksamensres, width=2, textvariable=karakter)
        ent_kar_reg.grid(row=3, column=4, padx=10, pady=10, sticky=W)

        #Knapper
        btn_lagre_reg=Button(reg_eksamensres, text='Lagre', command=registrer_eksresultat)
        btn_lagre_reg.grid(row=4, column=4, columnspan=2, padx=10, pady=10, sticky=W)

        btn_tilbake_reg=Button(reg_eksamensres, text='Tilbake', command=reg_eksamensres.destroy)
        btn_tilbake_reg.grid(row=5, column=5, padx=10, pady=10, sticky=W)

        #Binding
        lst_studenter.bind("<<ListboxSelect>>",hent_student)

        #Stenger markøren
        student_to_markor.close()

    #Oppretter hovedvindu
    eksamenresultat=Toplevel()
    eksamenresultat.title('Eksamensdatabase')

    #Overskrift
    lbl_overskrift=Label(eksamenresultat, text='USN - Eksamensresultat', font=('Helvetica Bold', 25))
    lbl_overskrift.grid(row=0, column=0, columnspan=3)

    #Knapper
    btn_leggtil=Button(eksamenresultat, text='Registrere nytt resultat', command=reg_eks_res)
    btn_leggtil.grid(row=2, column=0, padx=10, pady=10)

    btn_endre=Button(eksamenresultat, text='Endre eksamensresultat', command=endre_eks_res)
    btn_endre.grid(row=2, column=1, padx=10, pady=10)

    btn_slette=Button(eksamenresultat, text='Slett eksamensresultat', command=slette_eks_res)
    btn_slette.grid(row=2, column=2, padx=10, pady=10)

    btn_reg_samlet=Button(eksamenresultat, text=' Registrere samlet resultat', command=reg_samlet)
    btn_reg_samlet.grid(row=3, column=0, padx=10, pady=10)

    btn_kar_liste=Button(eksamenresultat, text='Karakterliste', command=kar_liste)
    btn_kar_liste.grid(row=3, column=1, padx=10, pady=10)

    btn_kar_stat=Button(eksamenresultat, text='Karakterfordeling', command=kar_stat)
    btn_kar_stat.grid(row=3, column=2, padx=10, pady=10)

    btn_kar_utskrift=Button(eksamenresultat, text='Utskrift eksamensresultater[K.P.7]', command=kule_punkt_7)
    btn_kar_utskrift.grid(row=4, column=0, padx=10, pady=10)

    btn_tilbake=Button(eksamenresultat, text='Hovedmeny', command=eksamenresultat.destroy)
    btn_tilbake.grid(row=5, column=3, padx=10, pady=10, sticky=E)


def eksamensdatabase():
    def utskrift_periode():
        def sok_eksamen():

            soke_markor=mindatabase.cursor()

            dato=sok.get()
            dato_2=sok_2.get()

            datetime.datetime.strptime(dato,"%Y-%m-%d")
            datetime.datetime.strptime(dato_2,"%Y-%m-%d")

            soke_markor.execute("SELECT Eksamen.* FROM Eksamen WHERE Dato >='%s' AND Dato <='%s'"%(dato,dato_2,))

            resultat=''
            for row in soke_markor:
                resultat += str(row[0]) + ' ' + ' ' + str(row[1]) + ' ' + str(row[2]) + '\n'
            soke_markor.close()

            #Lager en laber for resultatet
            lbl_res=Label(eksamen_periode, text=resultat, bd=2, font=('Helvetica', 10), justify='left')
            lbl_res.grid(row=2, column=0, columnspan=2, ipadx=10, ipady=10)

        eksamen_periode=Toplevel()
        eksamen_periode.title('Eksamensoversikt - Periode')

        #Utdata
        lbl_sok=Label(eksamen_periode, text='Søk dato, fra:')
        lbl_sok.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_sok_2=Label(eksamen_periode, text='Søk dato, til:')
        lbl_sok_2.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        #Inndata
        sok=StringVar()
        ent_sok=Entry(eksamen_periode, width=10, textvariable=sok)
        ent_sok.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        sok_2=StringVar()
        ent_sok_2=Entry(eksamen_periode, width=10, textvariable=sok_2)
        ent_sok_2.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #Knapper
        btn_sok=Button(eksamen_periode, text='Søk', command=sok_eksamen)
        btn_sok.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        btn_tilbake=Button(eksamen_periode, text='Tilbake', command=eksamen_periode.destroy)
        btn_tilbake.grid(row=3, column=3, padx=10, pady=10, sticky=W)

    def utskrift_dag():
        def sok_eksamen():
            
            soke_markor=mindatabase.cursor()

            dato=sok.get()

            datetime.datetime.strptime(dato,"%Y-%m-%d")

            soke_markor.execute("SELECT * FROM Eksamen WHERE Dato='%s'"%(dato,))

            resultat=''
            for row in soke_markor:
                resultat += str(row[0]) + ' ' + ' ' + str(row[1]) + ' ' + str(row[2]) + '\n' + '\n'
            soke_markor.close()

            #Lager en laber for resultatet
            lbl_res=Label(eksamen, text=resultat, bd=2, font=('Helvetica', 10), justify='left')
            lbl_res.grid(row=2, column=0, columnspan=2, ipadx=10, ipady=10)

        eksamen=Toplevel()
        eksamen.title('Eksamensoversikt')

        #Utdata
        lbl_sok=Label(eksamen, text='Søk dato:')
        lbl_sok.grid(row=0, column=0, padx=10, pady=10, sticky=E)

        #Inndata
        sok=StringVar()
        ent_sok=Entry(eksamen, width=10, textvariable=sok)
        ent_sok.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #Knapper
        btn_sok=Button(eksamen, text='Søk', command=sok_eksamen)
        btn_sok.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        btn_tilbake=Button(eksamen, text='Tilbake', command=eksamen.destroy)
        btn_tilbake.grid(row=3, column=3, padx=10, pady=10, sticky=W)

    #Oppretter nytt vindu samt flere def'er for sletting av eksamen
    def slett_eksamen():
        #Søke opp eksamen for sletting
        def sok_eksamen_slette():

            soke_slett_markor=mindatabase.cursor()

            valg=sok_slette.get()
            dato_slett=sok_dato.get()

            datetime.datetime.strptime(dato_slett,"%Y-%m-%d")

            soke_slett_markor.execute("SELECT Emnekode,Dato,Romnr FROM Eksamen WHERE Emnekode='%s' AND Dato='%s'"%(valg,dato_slett,))

            for row in soke_slett_markor:
                emnekode_slette.set(row[0])
                dato_slette.set(row[1])
                rom_slette.set(row[2])

        #Def for å slette eksamen
        def eks_slett():

            #Oppretter markør
            slette_eksamen_markor=mindatabase.cursor()

            emnekode=emnekode_slette.get()

            slett_eks="DELETE FROM Eksamen WHERE Emnekode ='%s' AND Emnekode NOT IN (SELECT Emnekode FROM Eksamensresultat)"%(emnekode,)

            slette_eksamen_markor.execute(slett_eks,(emnekode))
            
            #Bekrefter endringer til databasen
            mindatabase.commit()

            #Stenger markøren
            slette_eksamen_markor.close()

            #Stenger slette vindu
            slette_eksamen.destroy()

        #Oppretter Toplevel vindu
        slette_eksamen=Toplevel()
        slette_eksamen.title('Slette eksamen')

        #Utdata
        lbl_sok_slette=Label(slette_eksamen, text='Søk på emnekode:*')
        lbl_sok_slette.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_sok_dato=Label(slette_eksamen, text='Søk på dato:*')
        lbl_sok_dato.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_emnkode_slette=Label(slette_eksamen, text='Emnekode:')
        lbl_emnkode_slette.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        lbl_dato_slette=Label(slette_eksamen, text='Dato:')
        lbl_dato_slette.grid(row=4, column=0, padx=5, pady=5, sticky=E)

        lbl_rom_slette=Label(slette_eksamen, text='Romnr:')
        lbl_rom_slette.grid(row=5, column=0, padx=5, pady=5, sticky=E)

        #Inndata
        sok_slette=StringVar()
        ent_sok_slette=Entry(slette_eksamen, width=8, textvariable=sok_slette)
        ent_sok_slette.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        sok_dato=StringVar()
        ent_sok_dato=Entry(slette_eksamen, width=10, textvariable=sok_dato)
        ent_sok_dato.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        emnekode_slette=StringVar()
        ent_emnekode_slette=Entry(slette_eksamen, width=8, state='readonly', textvariable=emnekode_slette)
        ent_emnekode_slette.grid(row=3, column=1, padx=10, sticky=W)

        dato_slette=StringVar()
        ent_dato_slette=Entry(slette_eksamen, width=10, state='readonly', textvariable=dato_slette)
        ent_dato_slette.grid(row=4, column=1, padx=10, sticky=W)

        rom_slette=StringVar()
        ent_rom_slette=Entry(slette_eksamen, width=5, state='readonly', textvariable=rom_slette)
        ent_rom_slette.grid(row=5, column=1, padx=10, sticky=W)

        #Knapper
        btn_slette_tilbake=Button(slette_eksamen, text='Tilbake', command=slette_eksamen.destroy)
        btn_slette_tilbake.grid(row=10, column=2, padx=10, pady=10, sticky=W)

        btn_slette=Button(slette_eksamen, text='Slett', command=eks_slett)
        btn_slette.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        btn_sok_slette=Button(slette_eksamen, text='Søk', command=sok_eksamen_slette)
        btn_sok_slette.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    #Oppretter nytt vindu samt flere def'er for å gjennomføre endre eksamen 
    def endre_eksamen():
        #Def for å søke opp eksamen
        def sok_eksamen():

            soke_markor=mindatabase.cursor()

            valg=sok.get()
            dato_sok=sok_dato.get()
            datetime.datetime.strptime(dato_sok,"%Y-%m-%d")

            soke_markor.execute("SELECT Emnekode,Dato,Romnr FROM Eksamen WHERE Emnekode='%s' AND Dato='%s'"%(valg,dato_sok,))

            for row in soke_markor:
                emnekode_endre.set(row[0])
                dato_endre.set(row[1])
                rom_endre.set(row[2])

        #Def for endring av eksamen
        def eks_endre():
            endre_eksamen_markor=mindatabase.cursor()

            emnekode=emnekode_endre.get()
            dato=dato_endre.get()
            romnr=rom_endre.get()
            valg=sok.get()

            endre_eks=("UPDATE Eksamen SET Emnekode=%s,Dato=%s,Romnr=%s WHERE Emnekode=%s")

            datany_eksamen=(emnekode,dato,romnr,valg)

            endre_eksamen_markor.execute(endre_eks,datany_eksamen)
            
            #Bekrefter endringer til databasen
            mindatabase.commit()

            #Stenger markøren
            endre_eksamen_markor.close()

            #Avslutter vinduet når endring er gjennomført
            eksamen_endre.destroy()

        #Oppretter Toplevel vindu
        eksamen_endre=Toplevel()
        eksamen_endre.title('Endre eksamen')

        #Utdata
        lbl_sok_endre=Label(eksamen_endre, text='Søk på emnekode*')
        lbl_sok_endre.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_sok_dato=Label(eksamen_endre, text='Søk på dato*')
        lbl_sok_dato.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_emnkode=Label(eksamen_endre, text='Emnekode:')
        lbl_emnkode.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        lbl_dato=Label(eksamen_endre, text='Dato:')
        lbl_dato.grid(row=4, column=0, padx=5, pady=5, sticky=E)

        lbl_rom=Label(eksamen_endre, text='Romnr:')
        lbl_rom.grid(row=5, column=0, padx=5, pady=5, sticky=E)

        #Inndata
        sok=StringVar()
        ent_sok_endre=Entry(eksamen_endre, width=8, textvariable=sok)
        ent_sok_endre.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        sok_dato=StringVar()
        ent_dato_sok=Entry(eksamen_endre, width=10, textvariable=sok_dato)
        ent_dato_sok.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        emnekode_endre=StringVar()
        ent_emnekode_endre=Entry(eksamen_endre, width=8, state='readonly', textvariable=emnekode_endre)
        ent_emnekode_endre.grid(row=3, column=1, padx=5, sticky=W)

        dato_endre=StringVar()
        ent_dato_endre=Entry(eksamen_endre, width=10, state='readonly', textvariable=dato_endre)
        ent_dato_endre.grid(row=4, column=1, padx=5, sticky=W)

        rom_endre=StringVar()
        ent_rom_endre=Entry(eksamen_endre, width=5, textvariable=rom_endre)
        ent_rom_endre.grid(row=5, column=1, padx=5, sticky=W)

        #Knapp
        btn_endre_tilbake=Button(eksamen_endre, text='Tilbake', command=eksamen_endre.destroy)
        btn_endre_tilbake.grid(row=10, column=2, padx=5, pady=5, sticky=W)

        btn_endre=Button(eksamen_endre, text='Endre', command=eks_endre)
        btn_endre.grid(row=6, column=1, padx=5, pady=5, sticky=W)

        btn_sok_endre=Button(eksamen_endre, text='Søk', command=sok_eksamen)
        btn_sok_endre.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    #Nytt vindu og def'er for å registrere eksamen
    def registrer_eksamen():
        def reg_eksamen():

            #Opprette markør
            registrer_markor=mindatabase.cursor()

            emne_kode=emnekode.get()
            dato_endre=dato.get()
            rom_nr=rom.get()

            #Registrer eksamen
            leggtil_eksamen=("INSERT INTO Eksamen"
                            "(Emnekode,Dato,Romnr)"
                            "VALUES(%s,%s,%s)")

            datany_eks=(emne_kode,dato_endre,rom_nr)
            registrer_markor.execute(leggtil_eksamen,datany_eks)

            #Bekrefter
            mindatabase.commit()

            #Stenger markør
            registrer_markor.close()
            ent_emnekode.delete(0, END)
            ent_dato.delete(0, END)
            ent_rom.delete(0, END)
                            
        #Oppretter Toplevel vindu
        reg_eks=Toplevel()
        reg_eks.title('Registrer eksamen')

        #Utdata
        lbl_emnkode=Label(reg_eks, text='Emnekode:')
        lbl_emnkode.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_dato=Label(reg_eks, text='Dato:')
        lbl_dato.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_rom=Label(reg_eks, text='Romnr:')
        lbl_rom.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        
        #Inndata
        emnekode=StringVar()
        ent_emnekode=Entry(reg_eks, width=8, textvariable=emnekode)
        ent_emnekode.grid(row=0, column=1, padx=5, sticky=W)

        dato=StringVar()
        ent_dato=Entry(reg_eks, width=10, textvariable=dato)
        ent_dato.grid(row=1, column=1, padx=5, sticky=W)

        rom=StringVar()
        ent_rom=Entry(reg_eks, width=5, textvariable=rom)
        ent_rom.grid(row=2, column=1, padx=5, sticky=W)

        #Knapp
        btn_eks_tilbake=Button(reg_eks, text='Tilbake', command=reg_eks.destroy)
        btn_eks_tilbake.grid(row=10, column=2, padx=5, pady=5, sticky=W)

        btn_lagre=Button(reg_eks, text='Lagre', command=reg_eksamen)
        btn_lagre.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    #Oppretter vindu
    eksamen=Toplevel()
    eksamen.title('Eksamensdatabase')

    #Overskrift
    lbl_overskrift=Label(eksamen, text='USN - Eksamen', font=('Helvetica Bold', 25))
    lbl_overskrift.grid(row=0, column=0, columnspan=3)

    #Knapper for eksamen
    btn_leggtil=Button(eksamen, text='Registrere eksamen', command=registrer_eksamen)
    btn_leggtil.grid(row=2, column=0, padx=5, pady=5)

    btn_endre=Button(eksamen, text='Endre eksamen', command=endre_eksamen)
    btn_endre.grid(row=2, column=1, padx=5, pady=5)

    btn_slette=Button(eksamen, text='Slett eksamen', command=slett_eksamen)
    btn_slette.grid(row=2, column=2, padx=5, pady=5)

    btn_utskrift=Button(eksamen, text='Utskrift eksamens(dag)', command=utskrift_dag)
    btn_utskrift.grid(row=3, column=0, padx=5, pady=5)

    btn_utskrift=Button(eksamen, text='Utskrift eksamens(periode)',command=utskrift_periode)
    btn_utskrift.grid(row=3, column=1, padx=5, pady=5)

    btn_tilbake=Button(eksamen, text='Hovedmeny', command=eksamen.destroy)
    btn_tilbake.grid(row=4, column=3, padx=5, pady=5, sticky=E)

def studentdatabase():
    #Oppretter eget vindu for å Endre en student
    def endre_student():
        #Def for å oppdatere student
        def oppdater_student():
            oppdater_markor=mindatabase.cursor()

            studentnr=(studnr_endre.get())
            f_navn=(fornavn_endre.get())
            e_navn=(etternavn_endre.get())
            email=(epost_endre.get())
            tlf=(telefon_endre.get())
            valg_endre=(velg.get())
            
            oppdater_stud=("UPDATE Student SET Studentnr=%s,Fornavn=%s,Etternavn=%s,Epost=%s,Telefon=%s WHERE Studentnr=%s")

            datany_stud=(studentnr,f_navn,e_navn,email,tlf,valg_endre)

            oppdater_markor.execute(oppdater_stud,datany_stud)

            mindatabase.commit()
            oppdater_markor.close()

            endre.destroy()
    
        #Oppretter nytt Toplevel vindu
        endre=Toplevel()
        endre.title('Endre Student')

        #Utdata
        lbl_studnr_endre=Label(endre, text='Studentnr:')
        lbl_studnr_endre.grid(row=0, column=0, sticky=E)

        lbl_fornavn_endre=Label(endre, text='Fornavn:')
        lbl_fornavn_endre.grid(row=1, column=0, sticky=E)

        lbl_etternavn_endre=Label(endre, text='Etternavn:')
        lbl_etternavn_endre.grid(row=2, column=0, sticky=E)

        lbl_epost_endre=Label(endre, text='Epost:')
        lbl_epost_endre.grid(row=3, column=0, sticky=E)

        lbl_telefon_endre=Label(endre, text='Telefon:')
        lbl_telefon_endre.grid(row=4, column=0, sticky=E)

        #Inndata
        studnr_endre=StringVar()
        ent_studnr_endre=Entry(endre, width=7, textvariable=studnr_endre)
        ent_studnr_endre.grid(row=0, column=1, padx=5, sticky=W)

        fornavn_endre=StringVar()
        ent_fornavn_endre=Entry(endre, width=30, textvariable=fornavn_endre)
        ent_fornavn_endre.grid(row=1, column=1, padx=5, sticky=W)

        etternavn_endre=StringVar()
        ent_etternavn_endre=Entry(endre, width=20, textvariable=etternavn_endre)
        ent_etternavn_endre.grid(row=2, column=1, padx=5, sticky=W)

        epost_endre=StringVar()
        ent_epost_endre=Entry(endre, width=40, textvariable=epost_endre)
        ent_epost_endre.grid(row=3, column=1, padx=5, sticky=W)

        telefon_endre=StringVar()
        ent_telefon_endre=Entry(endre, width=8, textvariable=telefon_endre)
        ent_telefon_endre.grid(row=4, column=1, padx=5, sticky=W)

        #Knapp
        btn_lagre=Button(endre, text='Lagre endringer', command=oppdater_student)
        btn_lagre.grid(row=5, column=1,padx=5, pady=10, sticky=W)

        btn_tilbake=Button(endre, text='Tilbake', command=endre.destroy)
        btn_tilbake.grid(row=6, column=2, padx=5, pady=5, sticky=W)

        #Variabel for å hente ut informasjon fra Studentdatabasen
        valg=ent_valg.get()

        #Viser resultat fra database til tekstboksene i "Endre student"
        #Opprette markør
        endre_markor=mindatabase.cursor()
        endre_markor.execute("SELECT Studentnr,Fornavn,Etternavn,Epost,Telefon FROM Student")

        #Loop gjennom resultat
        for student in endre_markor:
            if valg==student[0]:
                studnr_endre.set(student[0])
                fornavn_endre.set(student[1])
                etternavn_endre.set(student[2])
                epost_endre.set(student[3])
                telefon_endre.set(student[4])

    #Funksjon for valget "Slett student" med eget vindu og readonly bokser
    def slett():
        #Funksjon for å slette en student
        def slette_student():
            #Oppretter markør
            slette_markor=mindatabase.cursor()

            brukervalg=velg.get()

            slette_stud="DELETE FROM Student WHERE Studentnr =%s AND Studentnr NOT IN (SELECT Studentnr FROM Eksamensresultat)"%(brukervalg,)
        
            slette_markor.execute(slette_stud,brukervalg)

            #Bekrefter endringer
            mindatabase.commit()
            #Stenger markøren
            slette_markor.close()

            #Stenger vinduet for sletting av student
            slette.destroy()
        
        #Oppretter nytt Toplevel vindu
        slette=Toplevel()
        slette.title('Slette Student')

        #Utdata
        lbl_studnr_slette=Label(slette, text='Studentnr:')
        lbl_studnr_slette.grid(row=0, column=0, sticky=E)

        lbl_fornavn_slette=Label(slette, text='Fornavn:')
        lbl_fornavn_slette.grid(row=1, column=0, sticky=E)

        lbl_etternavn_slette=Label(slette, text='Etternavn:')
        lbl_etternavn_slette.grid(row=2, column=0, sticky=E)

        lbl_epost_slette=Label(slette, text='Epost:')
        lbl_epost_slette.grid(row=3, column=0, sticky=E)

        lbl_telefon_slette=Label(slette, text='Telefon:')
        lbl_telefon_slette.grid(row=4, column=0, sticky=E)

        #Inndata
        studnr_slette=StringVar()
        ent_studnr_slette=Entry(slette, width=7, state='readonly', textvariable=studnr_slette)
        ent_studnr_slette.grid(row=0, column=1, padx=5, sticky=W)

        fornavn_slette=StringVar()
        ent_fornavn_slette=Entry(slette, width=30, state='readonly', textvariable=fornavn_slette)
        ent_fornavn_slette.grid(row=1, column=1, padx=5, sticky=W)

        etternavn_slette=StringVar()
        ent_etternavn_slette=Entry(slette, width=20, state='readonly', textvariable=etternavn_slette)
        ent_etternavn_slette.grid(row=2, column=1, padx=5, sticky=W)

        epost_slette=StringVar()
        ent_epost_slette=Entry(slette, width=40, state='readonly', textvariable=epost_slette)
        ent_epost_slette.grid(row=3, column=1, padx=5, sticky=W)

        telefon_slette=StringVar()
        ent_telefon_slette=Entry(slette, width=8, state='readonly', textvariable=telefon_slette)
        ent_telefon_slette.grid(row=4, column=1, padx=5, sticky=W)

        #Knapp
        btn_lagre=Button(slette, text='Slett student', command=slette_student)
        btn_lagre.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        btn_tilbake=Button(slette, text='Tilbake', command=slette.destroy)
        btn_tilbake.grid(row=6, column=2, padx=5, pady=5, sticky=W)

        #Variabel for å hente ut informasjon
        valg=ent_valg.get()

        #Viser resultat fra database i tekstboksene til "Slett student" (kun for visning, "readonly")
        #Opprette markør
        slett_markor=mindatabase.cursor()
        slett_markor.execute("SELECT Studentnr,Fornavn,Etternavn,Epost,Telefon FROM Student")

        #Loop gjennom resultat
        for student in slett_markor:
            if valg==student[0]:
                studnr_slette.set(student[0])
                fornavn_slette.set(student[1])
                etternavn_slette.set(student[2])
                epost_slette.set(student[3])
                telefon_slette.set(student[4])

    #Legg til student funksjon
    def leggtil_student():
        def generer_ny_studnr():
            #Oppretter markør
            studentnummer_markor=mindatabase.cursor()

            #Prøver å finne høyeste verdi på studentnr for så å implemntere ny student nytt studentnr
            studentnummer_markor.execute("SELECT (MAX(Studentnr) + 1) FROM Student")

            for row in studentnummer_markor:
                studnr_ny.set(round(row[0]))
            studentnummer_markor.close()

        def legg_til_student():
            leggtil_markor=mindatabase.cursor()
            
            #Henter informasjon for å legge til student
            studentnr=studnr_ny.get()
            f_navn=fornavn.get()
            e_navn=etternavn.get()
            e_post=epost.get()
            tlf=telefon.get()

            #Legg til studenter
            leggtil_stud=("INSERT INTO Student"
                        "(Studentnr,Fornavn,Etternavn,Epost,Telefon)"
                        "VALUES(%s,%s,%s,%s,%s)")

            datany_stud=(studentnr,f_navn,e_navn,e_post,tlf)
            leggtil_markor.execute(leggtil_stud,datany_stud)

            #Bekreft endring
            mindatabase.commit()
            
            #Stenger markøren
            leggtil_markor.close()

            ent_studnr_ny.delete(0, END)
            ent_fornavn.delete(0, END)
            ent_etternavn.delete(0, END)
            ent_epost.delete(0, END)
            ent_telefon.delete(0, END)
        
        #Oppretter vindu
        leggtil=Toplevel()
        leggtil.title('Registrer student')

        #Utdata
        lbl_studnr=Label(leggtil, text='Studentnr:')
        lbl_studnr.grid(row=0, column=0, sticky=E)

        lbl_fornavn=Label(leggtil, text='Fornavn:')
        lbl_fornavn.grid(row=1, column=0, sticky=E)

        lbl_etternavn=Label(leggtil, text='Etternavn:')
        lbl_etternavn.grid(row=2, column=0, sticky=E)

        lbl_epost=Label(leggtil, text='Epost:')
        lbl_epost.grid(row=3, column=0, sticky=E)

        lbl_telefon=Label(leggtil, text='Telefon:')
        lbl_telefon.grid(row=4, column=0, sticky=E)

        #Inndata
        studnr_ny=StringVar()
        ent_studnr_ny=Entry(leggtil, width=7, state='readonly', textvariable=studnr_ny)
        ent_studnr_ny.grid(row=0, column=1, padx=5, sticky=W)

        fornavn=StringVar()
        ent_fornavn=Entry(leggtil, width=30, textvariable=fornavn)
        ent_fornavn.grid(row=1, column=1, padx=5, sticky=W)

        etternavn=StringVar()
        ent_etternavn=Entry(leggtil, width=20, textvariable=etternavn)
        ent_etternavn.grid(row=2, column=1, padx=5, sticky=W)

        epost=StringVar()
        ent_epost=Entry(leggtil, width=40, textvariable=epost)
        ent_epost.grid(row=3, column=1, padx=5, sticky=W)

        telefon=StringVar()
        ent_telefon=Entry(leggtil, width=8, textvariable=telefon)
        ent_telefon.grid(row=4, column=1, padx=5, sticky=W)

        #Knapper
        btn_generer_studnr=Button(leggtil, text='Generer studentnr', command=generer_ny_studnr)
        btn_generer_studnr.grid(row=0, column=2, padx=5, pady=5, sticky=E)

        btn_lagre=Button(leggtil, text='Lagre', command=legg_til_student)
        btn_lagre.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        btn_avbryt=Button(leggtil, text='Tilbake', command=leggtil.destroy)
        btn_avbryt.grid(row=6, column=2, padx=5, pady=5, sticky=W)

    #Oppretter en funksjon som viser full informasjon om studenter som ligger i databasen med eget vindu
    def utskrift_student():
        #Oppretter vindu
        utskrift_vindu=Toplevel()
        utskrift_vindu.title('Komplett utskrift')

        utskrift=''
        utskrift_markor=mindatabase.cursor()

        #Henter resultat fra databasen
        utskrift_markor.execute("SELECT * FROM Student")

        #Looper gjennom resultatet
        utskrift=''

        for row in utskrift_markor:
            utskrift +=row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4] + '\n'

        #Lager label for utskriften
        lbl_utskrift=Label(utskrift_vindu, text=utskrift, bd=1, relief='sunken', font=('Helvetica', 10), justify='left')
        lbl_utskrift.grid(row=0, column=0, columnspan=2, ipadx=10, ipady=10)

        #Knapp for å navigere seg tilbake
        btn_tbk=Button(utskrift_vindu, text='Tilbake', command=utskrift_vindu.destroy)
        btn_tbk.grid(row=2, column=3, padx=5, pady=5)

    #Oppretter en funksjon for å vise studentnummer og studentens navn på forsiden for videre navigering
    def vis_res():

        print_markor=mindatabase.cursor()

        #Viser resultat fra database
        print_markor.execute("SELECT * FROM Student")
        
        #Looper gjennom resultater
        skriv_res=''
        for row in print_markor:
            skriv_res +=row[0] + ' ' + ' ' + row[1] + ' ' + row[2] + '\n'

        #Lager en Label for resultatet
        lbl_res=Label(student, text=skriv_res, bd=1, relief='sunken', font=('Helvetica', 10), justify='left')
        lbl_res.grid(row=7, column=0, columnspan=2, ipadx=10, ipady=10)

    #Oppretter vindu
    student=Toplevel()
    student.title('Studentdatabase')

    #Utdata
    lbl_slette=Label(student, text='Studentnr for autofyll:')
    lbl_slette.grid(row=0, column=0, sticky=E)

    #Inndata
    velg=StringVar()
    ent_valg=Entry(student, width=7, textvariable=velg)
    ent_valg.grid(row=0, column=1, padx=5, sticky=W)

    #Knapper
    btn_lagre=Button(student, text='Legg til student', command=leggtil_student)
    btn_lagre.grid(row=5, column=0, padx=5, pady=5)

    btn_utskrift=Button(student, text='Utskrift student', command=vis_res)
    btn_utskrift.grid(row=5, column=1, padx=5, pady=5)

    btn_slette=Button(student, text='Slette student', command=slett)
    btn_slette.grid(row=5, column=2, padx=5, pady=5)

    btn_endre=Button(student, text='Endre student', command=endre_student)
    btn_endre.grid(row=6, column=0, padx=5, pady=5)

    btn_utskrift=Button(student, text='Komplett utskrift', command=utskrift_student)
    btn_utskrift.grid(row=6, column=1, padx=5, pady=5)

    btn_tilbake=Button(student, text='Hovedmeny', command=student.destroy)
    btn_tilbake.grid(row=12, column=2, padx=5, pady=5, sticky=W)

#Kobler på databasen
mindatabase=mysql.connector.connect(host='yourConnectionString goes here')
#Feil på MYSQL
#' (Limes inn mellom user og db)

#Hovedvindu for applikasjonen
hovedvindu=Tk()
hovedvindu.title('USN - Utdanning')

#Overskrift
lbl_overskrift=Label(hovedvindu, text='USN - Utdanning', font=('Helvetica Bold', 25))
lbl_overskrift.grid(row=0, column=0, columnspan=2)

#Knapper for å navigere seg rundt applikasjonen
btn_student=Button(hovedvindu, text='Studentdatabase', command=studentdatabase)
btn_student.grid(row=2, column=0, padx=10, pady=10, ipadx=100)

btn_eksamen=Button(hovedvindu, text='Eksamensdatabase', command=eksamensdatabase)
btn_eksamen.grid(row=2, column=1, padx=10, pady=10, ipadx=100)

btn_vitnemal=Button(hovedvindu, text='Vitnemålsdatabase', command=vitnemal)
btn_vitnemal.grid(row=3, column=0, padx=10, pady=10, ipadx=95)

btn_eks_res=Button(hovedvindu, text='Eksamensresultat', command=eksamensresultat)
btn_eks_res.grid(row=3, column=1, padx=10, pady=10, ipadx=105)

btn_avslutt=Button(hovedvindu, text='Avslutt', command=hovedvindu.destroy)
btn_avslutt.grid(row=4, column=1, padx=5, pady=5, sticky=E)

hovedvindu.mainloop()

#Stenger databasen
mindatabase.close()