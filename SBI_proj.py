from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import webbrowser
import mysql.connector
import random
import numpy as np

"""

Auxiliary functions

"""
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

def tggl_fscreen():
        if tk . attributes('-fullscreen') == False:
            tk . attributes('-fullscreen', True)
        else:
            tk . attributes('-fullscreen', False)
            tk . state("zoomed")

def shift():
    x1,y1,x2,y2 = c_text.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = c_text.winfo_width()
        y1 = c_text.winfo_height()//2
        c_text.coords("marquee",x1,y1)
    else:
        c_text.move("marquee", -2, 0)
    c_text.after(1000//fps,shift)

def callback(url):
    webbrowser.open_new(url)


"""

Auxiliary functions

"""
tk = Tk()
tk . iconbitmap("X:/ishaan/_Data Science/SBI/img/sbi_logo.ico")
tk . attributes('-fullscreen', True)
#tk . geometry("1600x900")
tk . title("Welcome to SBI Net Banking")
tk . configure(background = "lightblue")

"""

Images

"""

fscreen = Image.open("X:/ishaan/_Data Science/SBI/img/fscreen.png") . resize((25, 25), Image.ANTIALIAS)
sbi_logo = Image.open("X:/ishaan/_Data Science/SBI/img/sbi_logo.png") . resize((280, 180), Image.ANTIALIAS)
pers_bnk = Image.open("X:/ishaan/_Data Science/SBI/img/pers_bankng.JPG") . resize((270, 88), Image.ANTIALIAS)
corp_bnk = Image.open("X:/ishaan/_Data Science/SBI/img/corp_bankng.JPG") . resize((388, 103), Image.ANTIALIAS)
lgn = Image.open("X:/ishaan/_Data Science/SBI/img/login.JPG") . resize((138, 38), Image.ANTIALIAS)
rgstr = Image.open("X:/ishaan/_Data Science/SBI/img/register.JPG") . resize((163, 51), Image.ANTIALIAS)
c_care = Image.open("X:/ishaan/_Data Science/SBI/img/cust_care.JPG") . resize((165, 55), Image.ANTIALIAS)
hlp = Image.open("X:/ishaan/_Data Science/SBI/img/help.JPG") . resize((133, 53), Image.ANTIALIAS)
m_lk = Image.open("X:/ishaan/_Data Science/SBI/img/more_links.JPG") . resize((168, 42), Image.ANTIALIAS)
bck = Image.open("X:/ishaan/_Data Science/SBI/img/back.png") . resize((60, 40), Image.ANTIALIAS)
capcha1 = Image.open("X:/ishaan/_Data Science/SBI/img/captcha/1.jpg") . resize((150, 53), Image.ANTIALIAS)
capcha2 = Image.open("X:/ishaan/_Data Science/SBI/img/captcha/2.jpg") . resize((150, 53), Image.ANTIALIAS)
capcha3 = Image.open("X:/ishaan/_Data Science/SBI/img/captcha/3.jpg") . resize((150, 53), Image.ANTIALIAS)
rld = Image.open("X:/ishaan/_Data Science/SBI/img/reload.jpg") . resize((20, 20), Image.ANTIALIAS)
lgn_wlc = Image.open("X:/ishaan/_Data Science/SBI/img/welc.jpg") . resize((1400, 40), Image.ANTIALIAS)
rnd_pic1 = Image.open("X:/ishaan/_Data Science/SBI/img/banner11.jpg") . resize((700, 380), Image.ANTIALIAS)
rnd_pic2 = Image.open("X:/ishaan/_Data Science/SBI/img/prec.jpg") . resize((1400, 200), Image.ANTIALIAS)
rnd_pic3 = Image.open("X:/ishaan/_Data Science/SBI/img/inst_login.jpg") . resize((700, 50), Image.ANTIALIAS)
prof_bg = Image.open("X:/ishaan/_Data Science/SBI/img/prof_bg.jpg") . resize((1600, 900), Image.ANTIALIAS)
ishaan_dp = Image.open("X:/ishaan/_Data Science/SBI/img/ishaan.jpg") . resize((150, 150), Image.ANTIALIAS)
pmts = Image.open("X:/ishaan/_Data Science/SBI/img/pay1.png") . resize((296, 191), Image.ANTIALIAS)
dpst = Image.open("X:/ishaan/_Data Science/SBI/img/deposit1.png") . resize((296, 191), Image.ANTIALIAS)
lns = Image.open("X:/ishaan/_Data Science/SBI/img/loans1.png") . resize((296, 191), Image.ANTIALIAS)
bnnr1 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner1.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr2 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner2.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr3 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner3.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr4 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner4.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr5 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner5.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr6 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner6.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr7 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner7.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr8 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner8.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr9 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner9.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr10 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner10.jpg") . resize((1200, 300), Image.ANTIALIAS)
bnnr11 = Image.open("X:/ishaan/_Data Science/SBI/banners/banner11.jpg") . resize((1200, 300), Image.ANTIALIAS)

fscreen = ImageTk.PhotoImage(fscreen)
sbi_logo = ImageTk.PhotoImage(sbi_logo)
pers_bnk = ImageTk.PhotoImage(pers_bnk)
corp_bnk = ImageTk.PhotoImage(corp_bnk)
lgn = ImageTk.PhotoImage(lgn)
rgstr = ImageTk.PhotoImage(rgstr)
c_care = ImageTk.PhotoImage(c_care)
hlp = ImageTk.PhotoImage(hlp)
m_lk = ImageTk.PhotoImage(m_lk)
bck = ImageTk.PhotoImage(bck)
capcha1 = ImageTk.PhotoImage(capcha1)
capcha2 = ImageTk.PhotoImage(capcha2)
capcha3 = ImageTk.PhotoImage(capcha3)
rld = ImageTk . PhotoImage(rld)
lgn_wlc = ImageTk . PhotoImage(lgn_wlc)
rnd_pic1 = ImageTk . PhotoImage(rnd_pic1)
rnd_pic2 = ImageTk . PhotoImage(rnd_pic2)
rnd_pic3 = ImageTk . PhotoImage(rnd_pic3)
prof_bg = ImageTk . PhotoImage(prof_bg)
ishaan_dp = ImageTk . PhotoImage(ishaan_dp)
pmts = ImageTk . PhotoImage(pmts)
dpst = ImageTk . PhotoImage(dpst)
lns = ImageTk . PhotoImage(lns)
bnnr1 = ImageTk . PhotoImage(bnnr1)
bnnr2 = ImageTk . PhotoImage(bnnr2)
bnnr3 = ImageTk . PhotoImage(bnnr3)
bnnr4 = ImageTk . PhotoImage(bnnr4)
bnnr5 = ImageTk . PhotoImage(bnnr5)
bnnr6 = ImageTk . PhotoImage(bnnr6)
bnnr7 = ImageTk . PhotoImage(bnnr7)
bnnr8 = ImageTk . PhotoImage(bnnr8)
bnnr9 = ImageTk . PhotoImage(bnnr9)
bnnr10 = ImageTk . PhotoImage(bnnr10)
bnnr11 = ImageTk . PhotoImage(bnnr11)

"""

Images

"""
#Captcha
captcha_ = [[capcha1, "my3xg"], [capcha2, "exnxm"], [capcha3, "7mgb8"]]
#Captcha
"""

Personal Banking

"""

details_cn = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
details_cur = details_cn . cursor()
details_cur . execute("select * from profile_details")
details_list = details_cur . fetchall()
i = 0
details_ = {}

for det in details_list:
    details_[det[1]] = det
    i += 1

details_cn . commit()
details_cn . close()

q_lst = ["What is your childhood friend's name?", "What is your favorite color?", "What was your first pet's name?", "Where were you born?", "What is your favorite food?", "What is the color of your eye?", "What is your favorite destination?"]

def prof_page(account):

    def dep_func(amnt):
        global blnc, cust_id
        blnc += float(amnt . get())
        deposit_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
        deposit_cur = deposit_cn . cursor()
        deposit_cur . execute("insert into account_balance (cust_id, deposit, balance) values ({},{}, {})" . format(cust_id, float(amnt . get()), blnc))
                
        deposit_cn . commit()
        deposit_cn . close()
        
        deposit1_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
        deposit1_cur = deposit1_cn . cursor()
        deposit1_cur . execute("select * from account_balance where trans_num = (select max(trans_num) from account_balance)")
        deposit_list_ = deposit1_cur . fetchall()
                
        deposit1_cn . commit()
        deposit1_cn . close()

        dep_l = []
        
        for tran in deposit_list_:
            for elem in tran:
                dep_l . append(elem)

        if r % 2 == 0:
            tree.insert('', 0, text = dep_l, values = dep_l, tags = ('oddrow',))
        else:
            tree.insert('', 0, text = dep_l, values = dep_l, tags = ('evenrow',))
        #print(dep_l)

        p_can . itemconfigure(cur_blnc,text = blnc)
        
    def wdraw_func(amnt):
        global blnc, cust_id
        blnc -= float(amnt . get())
        withdraw_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
        withdraw_cur = withdraw_cn . cursor()
        withdraw_cur . execute("insert into account_balance (cust_id, withdrawal, balance) values ({},{}, {})" . format(cust_id, float(amnt . get()), blnc))
                
        withdraw_cn . commit()
        withdraw_cn . close()
        
        withdraw1_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
        withdraw1_cur = withdraw1_cn . cursor()
        withdraw1_cur . execute("select * from account_balance where trans_num = (select max(trans_num) from account_balance)")
        withdraw_list_ = withdraw1_cur . fetchall()
                
        withdraw1_cn . commit()
        withdraw1_cn . close()

        wdraw_l = []
        
        for tran in withdraw_list_:
            for elem in tran:
                wdraw_l . append(elem)

        if r % 2 == 0:
            tree.insert('', 0, text = wdraw_l, values = wdraw_l, tags = ('oddrow',))
        else:
            tree.insert('', 0, text = wdraw_l, values = wdraw_l, tags = ('evenrow',))
        print(wdraw_l)

        p_can . itemconfigure(cur_blnc,text = blnc)
    
    def depos():
        if d . get() in dep_types:
            def calc_dep():

                if amt_dep . get() != "" and int_rt[d . get()] != "" and per_dep . get() != "":
                    def add_depos(a, i, d, f, t):
                        global cust_id
                        dep_typ = repr(t)
                        #print(dep_typ)
                        depo_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
                        depo_cur = depo_cn . cursor()
                        depo_cur . execute("insert into account_deposits (cust_id, deposit_type, deposit_amount, deposit_interest, deposit_duration, final_amount) values ({},{},{},{},{},{})" . format(cust_id, dep_typ, float(a), i, d, f))
                        
                        depo_cn . commit()
                        depo_cn . close()

                        depo1_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
                        depo1_cur = depo1_cn . cursor()
                        depo1_cur . execute("select * from account_deposits where deposit_id = (select max(deposit_id) from account_deposits)")
                        dept_lst = depo1_cur . fetchall()

                        depo1_cn . commit()
                        depo1_cn . close()
                        
                        dp_l = []
                        for tran in dept_lst:
                            for elem in tran:
                                dp_l . append(elem)

                        if r % 2 == 0:
                            tree_dep.insert('', 0, text = dp_l, values = dp_l, tags = ('oddrow',))
                        else:
                            tree_dep.insert('', 0, text = dp_l, values = dp_l, tags = ('evenrow',))
                        print(dp_l)
                else:
                    messagebox . showinfo("Error", "Fill all the fields")


                fin_amt = float(amt_dep.get()) * (1 +  ( float( int_rt[ d.get() ] ) * float( per_dep.get() ) / 100))
                fin_amt_txt = "Total Amount after {} years: " . format(per_dep.get()) + str(fin_amt)
                d_can . create_text(30, 250, text = fin_amt_txt, anchor = "nw")

                add_dep_btn = Button(d_can,text = "Make a Deposit", command = lambda: add_depos(amt_dep . get(), int_rt[d . get()], per_dep . get(), fin_amt, d . get()))
                d_can . create_window(160, 280, anchor = "nw", window = add_dep_btn)
            
            def chng_depos():
                i_r = "Interest Rate: " + str(int_rt[d.get()])
                d_can . itemconfig(d_typ, text = d.get())
                d_can . itemconfig(d_typ_int, text = i_r)

            
            d_can . delete(dep_chs_wind)
            dep_chg = Button(d_can, text = "Change Deposit", command = chng_depos)
            dep_chg_wind = d_can . create_window(30,80, anchor = "nw", window = dep_chg)
            i_r = "Interest Rate: " + str(int_rt[d.get()])
            d_typ = d_can . create_text(30, 120, text = d . get(), anchor = "nw")
            d_typ_int = d_can . create_text(30, 140, text = i_r, anchor = "nw")
            d_can . create_text(30, 170, text = "Amount to be deposited:", anchor = "nw")
            d_can . create_text(30, 190, text = "Period of deposit:", anchor = "nw")
            
            amt_dep = Entry(d_can)
            per_dep = Entry(d_can)
            amt_dep_wind = d_can . create_window(230, 170, anchor = "nw", window = amt_dep)
            per_dep_wind = d_can . create_window(230, 190, anchor = "nw", window = per_dep)

            but_dep = Button(d_can, text = "Calculate Total EMI", command = calc_dep)
            but_dep_wnd = d_can . create_window(140, 220, anchor = "nw", window = but_dep)
        
        else:
            messagebox . showinfo("Error", "Choose a deposit")

    def loans_get(loan_typ):
        def emi_calculation():
            if amnt_depo . get() != '' and tim_per . get() != '':
                calc_emi = float(amnt_depo . get()) * (float(tim_per . get()) * in_rate / 100)
                fin_amnt = float(amnt_depo . get()) + calc_emi

                l_can . itemconfigure(emi_lbl, text = calc_emi)
                l_can . itemconfigure(fam_lbl, text = fin_amnt)

                l_can . create_text(500,180, text = "TAKE Your FIRST STEP towards REALIZING your DREAMS", font = "Verdana 13 bold", anchor = "nw")
                
                def apply_now():
                    confirmed = messagebox . askyesno("Confirmation", "Are you sure you want to apply for the loan?")
                    if confirmed:
                        conf_loans_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
                        conf_loans_cur = conf_loans_cn . cursor()
                        conf_loans_cur . execute("insert into loans_hist (loan_type, loan_amount, loan_period, loan_interest, emi, final_amount, cust_id) values({}, {}, {}, {}, {}, {}, {})" . format(repr(loan_typ), float(amnt_depo . get()), float(tim_per . get()), in_rate, calc_emi, fin_amnt, cust_id))
                        
                        conf_loans_cn . commit()
                        conf_loans_cn . close()

                        conf_loans1_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
                        conf_loans1_cur = conf_loans1_cn . cursor()
                        conf_loans1_cur . execute("select * from loans_hist where loan_number = (select max(loan_number) from loans_hist)")
                        loan_list_ = conf_loans1_cur . fetchall()
                                
                        conf_loans1_cn . commit()
                        conf_loans1_cn . close()

                        loan_l = []
        
                        for tran in loan_list_:
                            for elem in tran:
                                loan_l . append(elem)

                        if l_var % 2 == 0:
                            tree_loans.insert('', 0, text = loan_l, values = loan_l, tags = ('oddrow',))
                        else:
                            tree_loans.insert('', 0, text = loan_l, values = loan_l, tags = ('evenrow',))

                # Apply for the loan link
                def on_enter_a(e):
                    apply_loan_txt . config(fg = "red")
                
                def on_leave_a(e):
                    apply_loan_txt . config(fg = "blue")

                apply_loan_txt = Label(l_can, text = "Apply for this Loan Now", background = "#F8F8F8", fg = "blue", font = ("Verdana 13 underline bold"), cursor="hand2")
                apply_loan_txt . bind("<Button-1>", lambda e: apply_now())
                apply_loan_txt . bind("<Enter>", on_enter_a)
                apply_loan_txt . bind("<Leave>", on_leave_a)
                apply_loan_txt . place(x = 650, y = 210)
            
            else:
                messagebox . showerror("Blank Field(s)", "All fields are required to be filled")

        if loan_typ in list(int_rt_ln . keys()):
            l_can . create_text(30,250, anchor = "nw", text = "Enter amount to be deposited:")
            l_can . create_text(30,280, anchor = "nw", text = "Interest Rate:")
            l_can . create_text(30,310, anchor = "nw", text = "Enter the time period of deposit:")

            in_rate = int_rt_ln[loan_typ]
            
            amnt_depo = Entry(l_can)
            l_can . create_window(250,250, anchor = "nw", window = amnt_depo)
            l_can . create_text(250,280, anchor = "nw", text = in_rate)
            tim_per = Entry(l_can)
            l_can . create_window(250,310, anchor = "nw", window = tim_per)

            emi_calc_btn = Button(l_can, text = "Calculate EMI", command = emi_calculation)
            emi_calc_btn_wind = l_can . create_window(100,350, anchor = "nw", window = emi_calc_btn)

            l_can . create_text(30,380, text = "EMI", anchor = "nw")
            l_can . create_text(30,410, text = "Final Amount", anchor = "nw")
            emi_lbl = l_can . create_text(250,380, text = "---", anchor = "nw")
            fam_lbl = l_can . create_text(250,410, text = "---", anchor = "nw")

        else:
            messagebox.showinfo("No Input", "Please select an option to proceed")

    def payments_func():
        payments_frm . tkraise()

    def deposits_func():
        deposits_frm . tkraise()
    
    def loans_func():
        loans_frm . tkraise()

    def updt_sec_ques():
        tu = Toplevel()

        tu.iconbitmap("X:/ishaan/_Data Science/SBI/img/sbi_logo.ico")
        tu.geometry("400x210")
        tu.title("Update Security Questions")
        tu.configure(background = "lightblue")

        def updt():
            updt_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
            updt_cur = updt_cn . cursor()
            updt_cur . execute("update login_credentials set sec_ques1 = {}, sec_ans1 = {}, sec_ques2 = {}, sec_ans2 = {}, sec_ques3 = {}, sec_ans3 = {} where cust_id = {};" . format(repr(n1 . get()), repr(a1 . get()), repr(n2 . get()),  repr(a2 . get()), repr(n3 . get()), repr(a3 . get()), cust_id))
                    
            updt_cn . commit()
            updt_cn . close()

        q1_u = Label(tu, text = "Choose your first question:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 00)
        a1_u = Label(tu, text = "Answer:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 30)
        q2_u = Label(tu, text = "Choose your second question:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 60)
        a2_u = Label(tu, text = "Answer:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 90)
        q3_u = Label(tu, text = "Choose your third question:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 120)
        a3_u = Label(tu, text = "Answer:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 150)

        n1 = StringVar()
        q1_chose = ttk.Combobox(tu, width = 32, textvariable = n1)
        q1_chose['values'] = (q_lst)
        q1_chose . place(x = 180, y = 00)
        
        n2 = StringVar()
        q2_chose = ttk.Combobox(tu, width = 32, textvariable = n2)
        q2_chose['values'] = (q_lst)
        q2_chose . place(x = 180, y = 60)
        
        n3 = StringVar()
        q3_chose = ttk.Combobox(tu, width = 32, textvariable = n3)
        q3_chose['values'] = (q_lst)
        q3_chose . place(x = 180, y = 120)

        a1 = StringVar()
        a2 = StringVar()
        a3 = StringVar()

        ans1_u = Entry(tu, textvariable = a1) . place(x = 180, y = 30)
        ans2_u = Entry(tu, textvariable = a2) . place(x = 180, y = 90)
        ans3_u = Entry(tu, textvariable = a3) . place(x = 180, y = 150)

        b_u = Button(tu, text = "Update", command = updt) . place(x = 100, y = 180)


    details_lst = details_[account]
    #print(details_lst)

    global cust_id
    cust_id = details_lst[0]

    def tggl_fscreen_prf():
        if tp . attributes('-fullscreen') == False:
            tp . attributes('-fullscreen', True)
        else:
            tp . attributes('-fullscreen', False)
            tp . state("zoomed")

    tp = Toplevel()
    tp . iconbitmap("X:/ishaan/_Data Science/SBI/img/sbi_logo.ico")
    tp . attributes('-fullscreen', True)
    tp . title("Profile")
    tp . configure(background = "lightblue")

    canvas_prof = Canvas(tp, width = 1600, height = 900, background = "lightblue")
    canvas_prof . place(x = 0, y = 0)
    
    prof_frame = Frame(canvas_prof, width = 1250, height = 650, bg = '#F8F8F8')
    prof_frame . place(x = 300, y = 200)

    bfscr_prf = Button(canvas_prof, image = fscreen, borderwidth = 0, command = tggl_fscreen_prf)
    bfscr_prf_wind = canvas_prof . create_window(1575, 0, anchor = "nw", window = bfscr_prf)

    # Canvas for details
    det_canvas = Canvas(canvas_prof, bg = "#1872AF", width = 1246, height = 160, borderwidth = 0)
    det_canvas . place(x = 300, y = 40)

    logo_pc = canvas_prof . create_image(10,10, anchor = "nw", image = sbi_logo)
    prf_pc = det_canvas . create_image(1090,7, anchor = "nw", image = ishaan_dp)
    prf_ttl = canvas_prof . create_text(750, 10, anchor = "nw", text = "PROFILE", font = "Arial 20 bold")

    name_frm = LabelFrame(det_canvas, text = "Name:", bg = "#1872AF", width = 40)
    full_name = str(details_lst[1]) + " " + str(details_lst[2]) + " " + str(details_lst[3])
    name_lbl = Label(name_frm, text = full_name, bg = "#1872AF", width = 40, justify = "left")
    name_frm . place(x = 20, y = 10)
    name_lbl . pack()

    custid_frm = LabelFrame(det_canvas, text = "Account Number:", bg = "#1872AF", width = 40)
    custid_lbl = Label(custid_frm, text = details_lst[4], bg = "#1872AF", width = 40)
    custid_frm . place(x = 20, y = 90)
    custid_lbl . pack()

    accnum_frm = LabelFrame(det_canvas, text = "IFSC Code:", bg = "#1872AF", width = 40)
    accnum_lbl = Label(accnum_frm, text = details_lst[5], bg = "#1872AF", width = 40)
    accnum_frm . place(x = 370, y = 90)
    accnum_lbl . pack()

    mailid_frm = LabelFrame(det_canvas, text = "Email ID:", bg = "#1872AF", width = 40)
    mailid_lbl = Label(mailid_frm, text = details_lst[6], bg = "#1872AF", width = 40)
    mailid_frm . place(x = 370, y = 10)
    mailid_lbl . pack()

    contct_frm = LabelFrame(det_canvas, text = "Contact Number:", bg = "#1872AF", width = 40)
    contct_lbl = Label(contct_frm, text = details_lst[7], bg = "#1872AF", width = 40)
    contct_frm . place(x = 720, y = 10)
    contct_lbl . pack()

    # Canvas for buttons
    opt_canvas = Canvas(canvas_prof, width = 298, height = 646, bg = '#1872AF')
    opt_canvas . place(x = 0, y = 200)

    # Payments button
    payments_btn = Button(opt_canvas, text = "Payments/Transfers", image = pmts, command = payments_func, font = "Arial 11", compound = TOP, bg = "#1872AF", borderwidth = 0, activebackground = "#14B2E2")
    payments_btn_wnd = opt_canvas . create_window(0,0, anchor = "nw", window = payments_btn)
    # Deposits Button
    deposit_btn = Button(opt_canvas, text = "Deposits", image = dpst, command = deposits_func, font = "Arial 11", compound = TOP, bg = "#1872AF", borderwidth = 0, activebackground = "#14B2E2")
    deposit_btn_wnd = opt_canvas . create_window(0,216, anchor = "nw", window = deposit_btn)
    # Loans Button
    loans_btn = Button(opt_canvas, text = "Apply for Loans", image = lns, command = loans_func, font = "Arial 11", compound = TOP, bg = "#1872AF", borderwidth = 0, activebackground = "#14B2E2")
    loans_btn_wnd = opt_canvas . create_window(0,432, anchor = "nw", window = loans_btn)

    # Payments Frame
    payments_frm = Frame(prof_frame, width = 1250, height = 650, bg = '#F8F8F8')
    payments_frm . place(x = 0, y = 0)

    p_can = Canvas(payments_frm, width = 1250, height = 650, bg = '#F8F8F8')
    p_can . place(x = 0, y = 0)

    # Getting balance 
    balance_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
    balance_cur = balance_cn . cursor()
    balance_cur . execute("select * from account_balance where cust_id = {}" . format(cust_id))
    balance_list = balance_cur . fetchall()

    global blnc
    blnc = balance_list[len(balance_list) - 1][4]
    
    balance_cn . commit()
    balance_cn . close()

    p_can . create_text(10, 50, text = "Current Balance: ", anchor = "nw")
    cur_blnc = p_can . create_text(100, 50, text = blnc, anchor = "nw")

    p_can . create_text(500, 80, text = "Make a Transaction:", font = "Helvetica 16 bold", anchor = "nw")
    p_can . create_text(325, 120, text = "Enter the amount to be deposited/withdrawn: ", font = "Helvetica 10 bold", anchor = "nw")

    amnt = StringVar()
    tran_entry = Entry(p_can, textvariable = amnt, width = 30)
    p_can . create_window(640, 120, window = tran_entry, anchor = "nw")

    dep_btn = Button(p_can, text = "Deposit", command = lambda: dep_func(amnt))
    wdr_btn = Button(p_can, text = "Withdraw", command = lambda: wdraw_func(amnt))
    p_can . create_window(500, 160, anchor = "nw", window = dep_btn)
    p_can . create_window(600, 160, anchor = "nw", window = wdr_btn)

    s = ttk . Style()
    s.theme_use('clam')

    p_can . create_text(575, 430, text = "Transactions:", font = "Helvetica 16 bold")
    
    # Add a Treeview widget for Transactions
    tree = ttk.Treeview(p_can, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)

    tree.column("# 1", anchor=CENTER, width = 120)
    tree.heading("# 1", text="Transaction Number")
    tree.column("# 2", anchor=CENTER, width = 200)
    tree.heading("# 2", text="Customer ID")
    tree.column("# 3", anchor=CENTER, width = 200)
    tree.heading("# 3", text="Deposit")
    tree.column("# 4", anchor=CENTER, width = 200)
    tree.heading("# 4", text="Withdraw")
    tree.column("# 5", anchor=CENTER, width = 200)
    tree.heading("# 5", text="Balance")
    

    tree.tag_configure('evenrow', background = 'white')
    tree.tag_configure('oddrow', background = 'lightblue')

    r = 0
    for tran in balance_list:
        trans = []
        for elem in tran:
            trans . append(elem)
        if r % 2 == 0:
            tree.insert('', 0, text = trans, values = trans, tags = ('oddrow',))
        else:
            tree.insert('', 0, text = trans, values = trans, tags = ('evenrow',))
        r += 1

    tree . place(x = 160, y = 450)

    # Deposits Frame
    deposits_frm = Frame(prof_frame, width = 1250, height = 650, bg = '#F8F8F8')
    deposits_frm . place(x = 0, y = 0)

    d_can = Canvas(deposits_frm, width = 1250, height = 650, bg = '#F8F8F8')
    d_can . place(x = 0, y = 0)

    dep_types = ["Fixed Deposit", "Recurring Deposit", "Systematic Investment Plan", "Public Provident Fund", "Joint Account", "Current Account"]
    int_rt = {"Fixed Deposit": 6.7, "Recurring Deposit": 7.3, "Systematic Investment Plan": 8.6, "Public Provident Fund": 9.2, "Joint Account": 2.7, "Current Account": 3.1}

    d_can . create_text(30, 30, text = "Choose your deposit type:", anchor = "nw")
    
    # Combobox
    d = StringVar()
    dep_chose = ttk.Combobox(d_can, width = 45, textvariable = d, state = "readonly")
    dep_chose['values'] = (dep_types)
    dep_chose . place(x = 30, y = 50)

    dep_chs = Button(d_can, text = "Choose Deposit", command = depos)
    dep_chs_wind = d_can . create_window(30,80, anchor = "nw", window = dep_chs)

    # Deposits history list
    depositd_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
    depositd_cur = depositd_cn . cursor()
    depositd_cur . execute("select * from account_deposits where cust_id = {}" . format(cust_id))
    depositd_list = depositd_cur . fetchall()

    
    depositd_cn . commit()
    depositd_cn . close()

    d_can . create_text(575, 430, text = "Deposits:", font = "Helvetica 16 bold")

    # Add a Treeview widget fo Deposits
    tree_dep = ttk.Treeview(d_can, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings', height=5)

    tree_dep.column("# 1", anchor=CENTER, width = 120)
    tree_dep.heading("# 1", text="Deposit ID")
    tree_dep.column("# 2", anchor=CENTER, width = 160)
    tree_dep.heading("# 2", text="Customer ID")
    tree_dep.column("# 3", anchor=CENTER, width = 160)
    tree_dep.heading("# 3", text="Deposit Type")
    tree_dep.column("# 4", anchor=CENTER, width = 160)
    tree_dep.heading("# 4", text="Deposit Amount")
    tree_dep.column("# 5", anchor=CENTER, width = 160)
    tree_dep.heading("# 5", text="Deposit Interest")
    tree_dep.column("# 6", anchor=CENTER, width = 160)
    tree_dep.heading("# 6", text="Deposit Duration")
    tree_dep.column("# 7", anchor=CENTER, width = 160)
    tree_dep.heading("# 7", text="Final Amount")
    

    tree_dep . tag_configure('evenrow', background = 'white')
    tree_dep . tag_configure('oddrow', background = 'lightblue')

    d_var = 0
    for tran in depositd_list:
        trans = []
        for elem in tran:
            trans . append(elem)
        if d_var % 2 == 0:
            tree_dep.insert('', 0, text = trans, values = trans, tags = ('oddrow',))
        else:
            tree_dep.insert('', 0, text = trans, values = trans, tags = ('evenrow',))
        d_var += 1

    tree_dep . place(x = 70, y = 450)


    # Loans Frame
    loans_frm = Frame(prof_frame, width = 1250, height = 650, bg = '#F8F8F8')
    loans_frm . place(x = 0, y = 0)

    l_can = Canvas(loans_frm, width = 1250, height = 650, bg = '#F8F8F8')
    l_can . place(x = 0, y = 0)

    l_can . create_text(30, 30, text = "Choose your required loan type:", anchor = "nw")
    l_can . create_text(250, 30, text = "EMI:", anchor = "nw")

    int_rt_ln = {"Home Loan": 6.65, "Student Loan": 3.5, "Personal Loan": 12.8, "Mortgage Loan": 7.6, "Small Business Loan": 5.9}
    #print(list(int_rt_ln . keys()))

    loan_type = StringVar()

    hom_l = Radiobutton(l_can, text = "Home Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Home Loan", variable = loan_type)
    stu_l = Radiobutton(l_can, text = "Student Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Student Loan", variable = loan_type)
    per_l = Radiobutton(l_can, text = "Personal Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Personal Loan", variable = loan_type)
    mrt_l = Radiobutton(l_can, text = "Mortgage Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Mortgage Loan", variable = loan_type)
    smb_l = Radiobutton(l_can, text = "Small Business Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Small Business Loan", variable = loan_type)

    hom_l_wind = l_can . create_window(30,50, anchor = "nw", window = hom_l)
    stu_l_wind = l_can . create_window(30,80, anchor = "nw", window = stu_l)
    per_l_wind = l_can . create_window(30,110, anchor = "nw", window = per_l)
    mrt_l_wind = l_can . create_window(30,140, anchor = "nw", window = mrt_l)
    smb_l_wind = l_can . create_window(30,170, anchor = "nw", window = smb_l)

    l_can . create_text(250, 55, text = "6.65%", anchor = "nw")
    l_can . create_text(250, 85, text = "3.5%", anchor = "nw")
    l_can . create_text(250, 115, text = "12.8%", anchor = "nw")
    l_can . create_text(250, 145, text = "7.6%", anchor = "nw")
    l_can . create_text(250, 175, text = "5.9%", anchor = "nw")
    
    clc_emi_btn = Button(l_can, text = "Select", command = lambda: loans_get(loan_type . get()))
    clc_emi_btn_wind = l_can . create_window(100,200, anchor = "nw", window = clc_emi_btn)

    # Loans history list
    loans_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
    loans_cur = loans_cn . cursor()
    loans_cur . execute("select * from loans_hist where cust_id = {}" . format(cust_id))
    loans_list = loans_cur . fetchall()
    #print(loans_list)
    
    loans_cn . commit()
    loans_cn . close()

    l_can . create_text(575, 430, text = "Loans:", font = "Helvetica 16 bold")

    # Add a Treeview widget for Loans
    tree_loans = ttk . Treeview(l_can, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings', height=5)

    tree_loans.column("# 1", anchor=CENTER, width = 100)
    tree_loans.heading("# 1", text="Customer ID")
    tree_loans.column("# 2", anchor=CENTER, width = 100)
    tree_loans.heading("# 2", text="Loan Number")
    tree_loans.column("# 3", anchor=CENTER, width = 150)
    tree_loans.heading("# 3", text="Loan Type")
    tree_loans.column("# 4", anchor=CENTER, width = 150)
    tree_loans.heading("# 4", text="Loan Amount")
    tree_loans.column("# 5", anchor=CENTER, width = 150)
    tree_loans.heading("# 5", text="Loan Period")
    tree_loans.column("# 6", anchor=CENTER, width = 150)
    tree_loans.heading("# 6", text="Loan Interest")
    tree_loans.column("# 7", anchor=CENTER, width = 150)
    tree_loans.heading("# 7", text="EMI")
    tree_loans.column("# 8", anchor=CENTER, width = 150)
    tree_loans.heading("# 8", text="Final Amount")
    

    tree_loans.tag_configure('evenrow', background = 'white')
    tree_loans.tag_configure('oddrow', background = 'lightblue')

    l_var = 0
    for tran in loans_list:
        trans = []
        for elem in tran:
            trans . append(elem)
        if l_var % 2 == 0:
            tree_loans.insert('', 0, text = trans, values = trans, tags = ('oddrow',))
        else:
            tree_loans.insert('', 0, text = trans, values = trans, tags = ('evenrow',))
        l_var += 1

    tree_loans . place(x = 80, y = 450)

    payments_frm . tkraise()

    # Update Security Questions link
    def on_enter_u(e):
        updt_sec_quess . config(font = "Verdana 10 underline", fg = "blue")
    
    def on_leave_u(e):
        updt_sec_quess . config(font = "Verdana 10", fg = "black")


    updt_sec_quess = Label(canvas_prof, text = "Update Security Questions", background = "lightblue", fg = "#30606e", font = ("Verdana 10"), cursor="hand2")
    updt_sec_quess . bind("<Button-1>", lambda e: updt_sec_ques())
    updt_sec_quess . bind("<Enter>", on_enter_u)
    updt_sec_quess . bind("<Leave>", on_leave_u)

    updt_sec_quess . place(x = 1375, y = 850)

#prof_page("Ishaan")

"""

Login Page

"""

capcha_sol = "my3xg"

def pers_bank_login():
    def tggl_fscreen_lg():
        if tl . attributes('-fullscreen') == False:
            tl . attributes('-fullscreen', True)
        else:
            tl . attributes('-fullscreen', False)
            tl . state("zoomed")
    
    def reset_entries():
        un_entry . delete(0, END)
        pw_entry . delete(0, END)
        capcha_entry . delete(0, END)

    def bck_2_hm():
        tk . attributes("-alpha", 1.0)
        tl . destroy()

    def capcha_refresh():
        rand_int = np . random . randint(3, size = 1)
        global capcha_sol
        if rand_int == 0:
            cl2 . itemconfig(capcha_img, image = capcha1)
            capcha_sol = "my3xg"
        elif rand_int == 1:
            cl2 . itemconfig(capcha_img, image = capcha2)
            capcha_sol = "exnxm"
        elif rand_int == 2:
            cl2 . itemconfig(capcha_img, image = capcha3)
            capcha_sol = "7mgb8"

    def profil():
        lgn_con = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
        lgn_cur = lgn_con . cursor()
        lgn_cur . execute("select  u_name, password from login_credentials")
        login_creds = lgn_cur . fetchall()
        
        #print(login_creds)
        for (x,y) in login_creds:
            if un_entry . get() == str(x) and pw_entry . get() == str(y):
                if capcha_entry . get() == capcha_sol:
                    prof_page(str(x))
                    tl . destroy()
                else:
                    messagebox.showinfo("Error", "Wrong captcha")
                break

        
        else:
            messagebox.showinfo("Error", "Username or password either wrong or does not exist")
        
        lgn_con . commit()
        lgn_con . close()
    
    def fgt_pss():
        def fnd_uname(inp):
            def chng(new_pass1, new_pass2, cust_id):
                print(cust_id, new_pass1)
                if new_pass1 == new_pass2:
                    creden_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
                    creden_cur = creden_cn . cursor()
                    creden_cur . execute("update login_credentials set password = {} where cust_id = {}" . format(repr(new_pass1), cust_id))
                    
                    creden_cn . commit()
                    creden_cn . close()
                
                else:
                    messagebox . showerror("Password Mismatch", "The entered passwords do not match")

            # Getting credentials 
            credent_cn = mysql.connector . connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
            credent_cur = credent_cn . cursor()
            credent_cur . execute("select * from login_credentials")
            credent_list = credent_cur . fetchall()
            
            credent_cn . commit()
            credent_cn . close()

            def chng_ps():
                    if ch_q . get() == acc_dt[4] and ch_a . get() == acc_dt[5]:
                        Label(tf, text = "Enter new password:", background =  "lightblue") . place(x = 10, y = 200)
                        Label(tf, text = "Confirm new password:", background =  "lightblue") . place(x = 10, y = 230)

                        ps1 = Entry(tf, show = "*")
                        ps2 = Entry(tf, show = "*")
                        ps1 . place(x = 190, y = 200)
                        ps2 . place(x = 190, y = 230)

                        chg_btn = Button(tf, text = "Change Password", command = lambda: chng(ps1 . get(), ps2 . get(), acc_dt[0]))
                        chg_btn . place(x = 140, y = 260)
                    
                    else:
                        messagebox . showerror("Wrong Input", "Kindly fill the correct details")
            
            for each_cred in credent_list:
                if inp == each_cred[1] or inp == each_cred[3]:
                    text_disp = "Username: " + str(each_cred[1]) 
                    Label(tf, text = text_disp, background =  "lightblue") . place(x = 10, y = 70)
                    Label(tf, text = "Choose your security question:", background =  "lightblue") . place(x = 10, y = 100)
                    Label(tf, text = "Enter your security answer:", background =  "lightblue") . place(x = 10, y = 130)

                    acc_dt = each_cred

                    ch_q = StringVar()
                    q_chose = ttk.Combobox(tf, width = 30, textvariable = ch_q)
                    q_chose['values'] = (q_lst)
                    q_chose . place(x = 190, y = 100)

                    ch_a = Entry(tf)
                    ch_a . place(x = 190, y = 130)

                    chng_ps_btn = Button(tf, text = "Submit", command = chng_ps)
                    chng_ps_btn . place(x = 160, y = 160)

                    break
                
                else:
                    messagebox . showerror("No such user in the database", "Kindly check the entered username/email address")

        tf = Toplevel()
        tf . iconbitmap("X:/ishaan/_Data Science/SBI/img/sbi_logo.ico")
        tf . title("Forgot Username/Password")
        tf . configure(background = "lightblue")
        tf . geometry("400x400")

        Label(tf, text = "Enter your username or email address:", background = "lightblue") . place(x = 10, y = 10)
        un_em = Entry(tf)
        un_em . place(x = 260, y = 10)

        sbmit = Button(tf, text = "Submit", command = lambda: fnd_uname(un_em . get()))
        sbmit . place(x = 160, y = 40)

        Label(tf, text = "** In case you don't remember your chosen security questions, contact your respective branch", background = "lightblue", font = "Verdana 6") . place(x = 5, y = 380)

    tl = Toplevel()
    tl . iconbitmap("X:/ishaan/_Data Science/SBI/img/sbi_logo.ico")
    tl . attributes('-fullscreen', True)
    tl . title("Login to SBI Net Banking")
    tl . configure(background = "lightblue")

    mlFrame = Frame(tl, width = 1600, height = 1600, bg = 'lightblue', highlightthickness=0)
    mlFrame . pack(fill = BOTH, expand = YES)

    canv_l = Canvas(mlFrame, width = 1600, height = 1600, bg = 'lightblue', highlightthickness=0)

    sb2 = Scrollbar(mlFrame, orient = VERTICAL, command = canv_l . yview)
    sb2 . pack(side = RIGHT, fill = Y)

    canv_l . config(yscrollcommand = sb2 . set)
    canv_l . pack(side = LEFT, fill=BOTH, expand=YES)

    ml1Frame = Frame(canv_l)
    ml1Frame . pack(fill = BOTH, expand = YES)
    canv_l . create_window((0,0), window = ml1Frame, anchor = "nw")

    cl1 = Canvas(ml1Frame, width = 1600, height = 900, bg = 'lightblue', highlightthickness=0)
    cl1 . pack()

    cl1 . bind("<Configure>", lambda e2: canv_l . configure(scrollregion = canv_l . bbox("all")))

    bfscr_lgn = Button(cl1, image = fscreen, borderwidth = 0, command = tggl_fscreen_lg)
    bfscr_lgn_wind = cl1 . create_window(1555, 0, anchor = "nw", window = bfscr_lgn)

    # Login Credentials Frame Start

    cl2 = Canvas(cl1, width = 1400, height = 700, bg = '#F8F8F8')
    cl2 . place (x = 100, y = 100)

    bck_btn = Button(cl2, image = bck, command = bck_2_hm)
    bck_btn . place(x = 20, y = 20)

    wlc_img = cl2 . create_image(0, 80, anchor = "nw", image = lgn_wlc)
    rnd_img1 = cl2 . create_image(700, 120, anchor = "nw", image = rnd_pic1)
    rnd_img2 = cl2 . create_image(0, 500, anchor = "nw", image = rnd_pic2)
    rnd_img3 = cl2 . create_image(0, 450, anchor = "nw", image = rnd_pic3)
    u_name = cl2 . create_text(120, 150, anchor = "nw", text = "Username: *", font = ('Helvetica 10 bold'))
    un_entry = Entry(tl, bg = "#D6DBDF")
    pw = cl2 . create_text(120, 200, anchor = "nw", text = "Password: *", font = ('Helvetica 10 bold'))
    pw_entry = Entry(tl, bg = "#D6DBDF", show = "*")
    un_window = cl2 . create_window(120, 175, anchor = "nw", window = un_entry)
    pw_window = cl2 . create_window(120, 225, anchor = "nw", window = pw_entry)
    capcha = cl2 . create_text(120, 250, anchor = "nw", text = "Enter the Captcha: *", font = ('Helvetica 10 bold'))
    capcha_entry = Entry(tl, bg = "#D6DBDF")
    capcha_window = cl2 . create_window(120, 275, anchor = "nw", window = capcha_entry)
    capcha_img = cl2 . create_image(120, 300, anchor = "nw", image = capcha1)
    
    rld_btn = Button(cl2, image = rld, borderwidth = 0, command = capcha_refresh)
    rld_btn . place(x = 250,y = 275)
    lgn_btn = Button(cl2, text = "Login", bg = "#2E86C1", fg = "white", command = profil)
    lgn_btn . place(x = 120, y = 365)
    rst_btn = Button(cl2, text = "Reset", bg = "#2E86C1", fg = "white", command = reset_entries)
    rst_btn . place(x = 180, y = 365)

    # Bind enter key with login button(Just link with the login function not the button itself)
    tl . bind("<Return>", lambda e: profil())

    fgt_pw = Label(cl2, text = "Forgot Login Username/Password?", background = "#F8F8F8", fg = "#30606e", font = ("Helvetica 10"), cursor="hand2")
    fgt_pw . bind("<Button-1>", lambda e: fgt_pss())
    fgt_pw . place(x = 300, y = 200)
    
    # Login Credentials Frame End
    
    tk . attributes("-alpha", 0)


"""

Login Page

"""

"""

Registration Page

"""

capcha_sol = "my3xg"
def pers_bank_reg():
    def tggl_fscreen_reg():
        if tr . attributes('-fullscreen') == False:
            tr . attributes('-fullscreen', True)
        else:
            tr . attributes('-fullscreen', False)
            tr . state("zoomed")
    
    def reset_entries():
        un_entry . delete(0, END)
        pw_entry . delete(0, END)
        capcha_entry . delete(0, END)

    def bck_2_hm():
        tk . attributes("-alpha", 1.0)
        tr . destroy()

    def capcha_refresh():
        rand_int = np . random . randint(3, size = 1)
        global capcha_sol
        if rand_int == 0:
            cl2 . itemconfig(capcha_img, image = capcha1)
            capcha_sol = "my3xg"
        elif rand_int == 1:
            cl2 . itemconfig(capcha_img, image = capcha2)
            capcha_sol = "exnxm"
        elif rand_int == 2:
            cl2 . itemconfig(capcha_img, image = capcha3)
            capcha_sol = "7mgb8"

    def reg_uname(uname, pw, captcha, q1, a1, q2, a2, q3, a3):
        ifsc_cde = "AXSB00001"
        
        id_con = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
        id_cur = id_con . cursor()
        id_cur . execute("select max(cust_id) from login_credentials")
        
        id_lst = id_cur . fetchall()
        id = int(id_lst[0][0]) + 1
        print(id)
        id_con . commit()
        id_con . close()
        
        if uname == "" or pw == "" or q1 == "" or a1 == "" or q2 == "" or a2 == "" or q3 == "" or a3 == "":
            messagebox . showerror("Field(s) empty", "All the fields are mandatory")
        
        else:
            if captcha == capcha_sol:
                reg_con = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='sbi_proj')
                reg_cur = reg_con . cursor()
                reg_cur . execute("insert into login_credentials (cust_id, u_name, password, sec_ques1, sec_ans1, sec_ques2, sec_ans2, sec_ques3, sec_ans3) values ({}, {}, {}, {}, {}, {}, {}, {}, {})" . format(id, repr(uname), repr(pw), repr(q1), repr(a1), repr(q2), repr(a2), repr(q3), repr(a3)))

                reg_con . commit()
                reg_con . close()
            
            else:
                messagebox . showerror("Wrong Captcha", "Enter the correct captcha")

    tr = Toplevel()
    tr . iconbitmap("X:/ishaan/_Data Science/SBI/img/sbi_logo.ico")
    tr . attributes('-fullscreen', True)
    tr . title("Register to SBI Net Banking")
    tr . configure(background = "lightblue")

    mlFrame = Frame(tr, width = 1600, height = 1600, bg = 'lightblue', highlightthickness=0)
    mlFrame . pack(fill = BOTH, expand = YES)

    canv_l = Canvas(mlFrame, width = 1600, height = 1600, bg = 'lightblue', highlightthickness=0)

    sb2 = Scrollbar(mlFrame, orient = VERTICAL, command = canv_l . yview)
    sb2 . pack(side = RIGHT, fill = Y)

    canv_l . config(yscrollcommand = sb2 . set)
    canv_l . pack(side = LEFT, fill=BOTH, expand=YES)

    ml1Frame = Frame(canv_l)
    ml1Frame . pack(fill = BOTH, expand = YES)
    canv_l . create_window((0,0), window = ml1Frame, anchor = "nw")

    cl1 = Canvas(ml1Frame, width = 1600, height = 900, bg = 'lightblue', highlightthickness=0)
    cl1 . pack()

    cl1 . bind("<Configure>", lambda e2: canv_l . configure(scrollregion = canv_l . bbox("all")))

    bfscr_lgn = Button(cl1, image = fscreen, borderwidth = 0, command = tggl_fscreen_reg)
    bfscr_lgn_wind = cl1 . create_window(1555, 0, anchor = "nw", window = bfscr_lgn)

    # Register Credentials Frame Start

    cl2 = Canvas(cl1, width = 1400, height = 700, bg = '#F8F8F8')
    cl2 . place (x = 100, y = 100)

    bck_btn = Button(cl2, image = bck, command = bck_2_hm)
    bck_btn . place(x = 20, y = 20)

    wlc_img = cl2 . create_image(0, 80, anchor = "nw", image = lgn_wlc)
    rnd_img1 = cl2 . create_image(700, 120, anchor = "nw", image = rnd_pic1)
    rnd_img2 = cl2 . create_image(0, 500, anchor = "nw", image = rnd_pic2)
    rnd_img3 = cl2 . create_image(0, 450, anchor = "nw", image = rnd_pic3)
    u_name = cl2 . create_text(120, 150, anchor = "nw", text = "Username: *", font = ('Helvetica 10 bold'))
    un_entry = Entry(tr, bg = "#D6DBDF")
    pw = cl2 . create_text(120, 200, anchor = "nw", text = "Password: *", font = ('Helvetica 10 bold'))
    pw_entry = Entry(tr, bg = "#D6DBDF", show = "*")
    un_window = cl2 . create_window(120, 175, anchor = "nw", window = un_entry)
    pw_window = cl2 . create_window(120, 225, anchor = "nw", window = pw_entry)
    capcha = cl2 . create_text(120, 250, anchor = "nw", text = "Enter the Captcha: *", font = ('Helvetica 10 bold'))
    capcha_entry = Entry(tr, bg = "#D6DBDF")
    capcha_window = cl2 . create_window(120, 275, anchor = "nw", window = capcha_entry)
    capcha_img = cl2 . create_image(120, 300, anchor = "nw", image = capcha1)

    # Security Questions

    combostyle = ttk.Style()

    combostyle.theme_create('combostyle', parent='alt',
                            settings = {'TCombobox':
                                        {'configure':
                                        {'selectbackground': '#D6DBDF',
                                        'fieldbackground': '#D6DBDF',
                                        'background': '#D6DBDF',
                                        'selectforeground': 'black'
                                        }}}
                            )

    combostyle.theme_use('combostyle')

    n1 = StringVar()
    q1_chose = ttk.Combobox(cl2, width = 32, textvariable = n1)
    q1_chose['values'] = (q_lst)
    q1_chose . place(x = 450, y = 175)
    
    n2 = StringVar()
    q2_chose = ttk.Combobox(cl2, width = 32, textvariable = n2)
    q2_chose['values'] = (q_lst)
    q2_chose . place(x = 450, y = 225)
    
    n3 = StringVar()
    q3_chose = ttk.Combobox(cl2, width = 32, textvariable = n3)
    q3_chose['values'] = (q_lst)
    q3_chose . place(x = 450, y = 275)

    sq1 = cl2 . create_text(300, 175, anchor = "nw", text = "Security Question 1: *", font = ('Helvetica 10 bold'))
    sq2 = cl2 . create_text(300, 225, anchor = "nw", text = "Security Question 2: *", font = ('Helvetica 10 bold'))
    sq3 = cl2 . create_text(300, 275, anchor = "nw", text = "Security Question 3: *", font = ('Helvetica 10 bold'))

    sa1 = cl2 . create_text(376, 200, anchor = "nw", text = "Answer: *", font = ('Helvetica 10 bold'))
    sa2 = cl2 . create_text(376, 250, anchor = "nw", text = "Answer: *", font = ('Helvetica 10 bold'))
    sa3 = cl2 . create_text(376, 300, anchor = "nw", text = "Answer: *", font = ('Helvetica 10 bold'))

    a1 = Entry(tr, bg = "#D6DBDF")
    a2 = Entry(tr, bg = "#D6DBDF")
    a3 = Entry(tr, bg = "#D6DBDF")

    a1_wind = cl2 . create_window(450, 200, anchor = "nw", window = a1)
    a2_wind = cl2 . create_window(450, 250, anchor = "nw", window = a2)
    a3_wind = cl2 . create_window(450, 300, anchor = "nw", window = a3)

    rld_btn = Button(cl2, image = rld, borderwidth = 0, command = capcha_refresh)
    rld_btn . place(x = 250,y = 275)
    reg_btn = Button(cl2, text = "Register", bg = "#2E86C1", fg = "white", command = lambda: reg_uname(un_entry . get(), pw_entry . get(), capcha_entry . get(), n1 . get(), a1 . get(), n2 . get(), a2 . get(), n3 . get(), a3 . get()))
    reg_btn . place(x = 280, y = 365)
    rst_btn = Button(cl2, text = "Reset", bg = "#2E86C1", fg = "white", command = reset_entries)
    rst_btn . place(x = 360, y = 365)

    # Bind enter key with register button(Just link with the login function not the button itself)
    tr . bind("<Return>", lambda e: reg_uname(un_entry . get(), pw_entry . get(), capcha_entry . get(), n1 . get(), a1 . get(), n2 . get(), a2 . get(), n3 . get(), a3 . get()))

    
    # Login Credentials Frame End
    
    tk . attributes("-alpha", 0)

"""

Registration Page

"""


"""

Personal Banking

"""


"""

Main Page

"""

mFrame = Frame(tk)
mFrame . pack(fill = BOTH, expand = YES)   

canv = Canvas(mFrame)

sb1 = Scrollbar(mFrame, orient = VERTICAL, command = canv . yview)
sb1 . pack(side = RIGHT, fill = Y)

canv . config(yscrollcommand = sb1 . set)
canv . pack(side = LEFT, fill=BOTH, expand=YES)


m1Frame = Frame(canv)
m1Frame . pack(fill = BOTH, expand = YES)
canv . create_window((0,0), window = m1Frame, anchor = "nw")

c1 = Canvas(m1Frame, width = 1600, height = 1600, bg = 'lightblue', highlightthickness=0)
c1 . pack()
c1 . bind("<Configure>", lambda e1: canv . configure(scrollregion = canv . bbox("all")))


bfscr = Button(c1, image = fscreen, borderwidth = 0, command = tggl_fscreen)
bfscr_wind = c1 . create_window(1555, 0, anchor = "nw", window = bfscr)

#Personal banking Frame
c2 = Canvas(c1, width = 600, height = 350, bg = '#F8F8F8')
c2 . place (x = 100, y = 30)

# Personal Banking image
pers_bnk_lbl = Label(c1, image = pers_bnk, borderwidth = 0)
pers_bnk_lbl . place(x = 260, y = 80)

# Login Button
lgn_pb = Button(c1, image = lgn, borderwidth = 0, command = pers_bank_login , cursor="hand2")
lgn_pb . place(x = 310, y = 180)

# Registration, Contact Us and Help Buttons
rgstr_pb = Button(c1, image = rgstr, borderwidth = 0, cursor="hand2", command = pers_bank_reg)
c2 . create_line(228,220, 228,275, fill = "grey")
hlp_pb =  Button(c1, image = hlp, borderwidth = 0, cursor="hand2")
c2 . create_line(388,220, 388,275, fill = "grey")
ccare_pb = Button(c1, image = c_care, borderwidth = 0, cursor="hand2")

rgstr_pb . place(x = 150, y = 250)
hlp_pb . place(x = 340, y = 250)
ccare_pb . place(x = 500, y = 250)

#Corporate banking Frame
c3 = Canvas(c1, width = 600, height = 350, bg = '#F8F8F8')
c3 . place (x = 810, y = 30)

# Corporate Banking image
corp_bnk_lbl = Label(c1, image = corp_bnk, borderwidth = 0)
corp_bnk_lbl . place(x = 920, y = 80)

# Registration, Contact Us and Help Buttons
rgstr_cb = Button(c1, image = rgstr, borderwidth = 0, cursor="hand2")
c3 . create_line(228,220, 228,275, fill = "grey")
hlp_cb =  Button(c1, image = hlp, borderwidth = 0, cursor="hand2")
c3 . create_line(388,220, 388,275, fill = "grey")
ccare_cb = Button(c1, image = c_care, borderwidth = 0, cursor="hand2")

rgstr_cb . place(x = 860, y = 250)
hlp_cb . place(x = 1050, y = 250)
ccare_cb . place(x = 1210, y = 250)

#Links Placement Start
links_ = [
        ["SBI Salary Account", "https://bank.sbi/web/salary-account"], 
        ["Linking of PAN with Aadhaar", "https://eportal.incometax.gov.in/iec/foservices/#/pre-login/bl-link-aadhaar"],
        ["Registration for Doorstep Banking", "https://psbdsb.in/"],
        ["Fair Lending Practice Code", "https://www.onlinesbi.com/documents/Yono_Business_Fair_Practice_Lending_Code.pdf"],
        ["Purchase Insurance Policy", "https://www.sbiyono.sbi/wps/portal/login"],
        ["SBI General Insurance Document Download", "https://www.sbigeneral.in/portal/downloads"],
        ["SBI FasTag", "https://fastag.onlinesbi.com/"],
        ["SBI Mutual Fund", "https://www.sbimf.com/en-us/quick-invest?arn_code=ARN12195"],
        ["NRI Services", "https://bank.sbi/web/nri/home"],
        ["Customer Complaint Form", "https://crcf.sbi.co.in/"],
        ["SBICAP Securities", "http://www.sbismart.com/"],
        ["SBICAP Trustee Company Ltd", "http://www.sbicaptrustee.com/"],
        ["SBI Express Remit", "https://remit.onlinesbi.com/"],
        ["Customer Request and Complaint Form (NEW)", "https://crcf.sbi.co.in/"],
        ["SBI Life Insurance", "http://www.sbilife.co.in/"],
        ["SBI Card", "http://www.sbicard.com/"],
        ["OnlineSBI Global", "https://www.onlinesbiglobal.com/"],
        ["Foreign Travel/EZ-Pay/Gift Cards", "https://prepaid.onlinesbi.com/"],
        ["SBI General Insurance", "http://www.sbigeneral.in/"],
        ["Service charges for non-maintenance of Average Balance in SB accounts", ""],
        ["CASH@SBI", "https://www.sbi.co.in/portal/web/home/cash-at-sbi"],
        ["State Bank Loyalty Rewardz", "https://www.rewardz.sbi/"],
        ["EPF", "https://www.onlinesbi.com/prelogin/epfohome.htm"],
        ["Online Locker Enquiry", "https://retail.onlinesbi.com/preretail/prelogineLockerInitial.htm"],
        ["Loan Against Shares", "https://retail.onlinesbi.com/las/loanagainstsharesinit.htm"],
        ["GSTN Updation", "https://www.onlinesbi.com/documents/GSTN_Transactions_Updation_Process.pdf"],
        ["eSBTR Challan Generation", "https://esbtr.onlinesbi.com/ESBTR1/OnlineReg.do?method=fetchDistrictList"],
        ["Donate - Kerala Floods", "https://kerala.gov.in/home"],
        ["Noida Metro Card", "https://retail.onlinesbi.com/sbijava/retail/html/faq_noida_metro.html"],
        ["SBICAP Trustee Company Ltd My WILL Services Online", "https://sbicaptrustee.in/mywill/index.jsp"],
        ["Nagpur Metro Card", "https://retail.onlinesbi.com/sbijava/retail/html/faq_nagpur_metro.html"],
        ["COVID-19 EMI Deferment", "https://bank.sbi/stopemi"],
        ["PM Mudra Yojana", "https://sbi.co.in/web/business/sme/sme-loans/pm-mudra-yojana"]
        ]

y_pos = 0

c4 = Canvas(c1, width = 1200, height = 300, bg = '#F8F8F8')
c4 . place(x = 150, y = 450)


for i in range(len(links_)):
    exec(f'def on_enter{i}(e):   link_label_{i} . config(font = "Verdana 10 underline", fg = "blue")')
    exec(f'def on_leave{i}(e):   link_label_{i} . config(font = "Verdana 10", fg = "black")')


for i in range(len(links_)):
    exec(f'link_label_{i} = Label(c4, text = links_[{i}][0], background = "#F8F8F8", fg = "#30606e", font = ("Verdana 10"), cursor="hand2")')
    exec(f'link_label_{i} . bind("<Button-1>", lambda e: callback(links_[{i}][1]))')
    exec(f'link_label_{i} . bind("<Enter>", on_enter{i})')
    exec(f'link_label_{i} . bind("<Leave>", on_leave{i})')

    if i < 16:
        if i % 4 == 0:
            y_pos += 50
            exec(f'link_label_{i} . place(x = 50, y = y_pos)')
        elif i % 4 == 1:
            exec(f'link_label_{i} . place(x = 300, y = y_pos)')
        elif i % 4 == 2:
            exec(f'link_label_{i} . place(x = 680, y = y_pos)')
        elif i % 4 == 3:
            exec(f'link_label_{i} . place(x = 950, y = y_pos)')
            
y_chng = 0

def more_lnks():
    
    def less_links():
        for i in range(16, len(links_)):
            exec(f'link_label_{i} . place_forget()')

        les_lnks . place_forget()
        mor_lnks . place(x = 500, y = 250)
        c4 . configure(height = 300)

    global y_chng
    for i in range(16, len(links_)):
        if i % 4 == 0:
            y_chng += 50
            exec(f'link_label_{i} . place(x = 50, y = y_pos + y_chng)')
        elif i % 4 == 1:
            exec(f'link_label_{i} . place(x = 300, y = y_pos + y_chng)')
        elif i % 4 == 2:
            exec(f'link_label_{i} . place(x = 680, y = y_pos + y_chng)')
        elif i % 4 == 3:
            exec(f'link_label_{i} . place(x = 950, y = y_pos + y_chng)')
    
    c4 . configure(height = y_pos + y_chng + 100)
    mor_lnks . place_forget()
    les_lnks = Button(c4, image = m_lk, command = less_links, borderwidth = 0)
    les_lnks . place(x = 500, y = y_pos + y_chng + 50)
    y_chng = 0
    

mor_lnks = Button(c4, image = m_lk, command = more_lnks, borderwidth = 0)
mor_lnks . place(x = 500, y = 250)

#Links Placement End

# Moving Text Starts
moving_text = "All citizens are requested to take e-pledge by visiting CVC’s website. Path for online “Integrity Pledge” is https://pledge.cvc.nic.in. Amalgamation of banks has been effected from 01-04-2021. Kindly delete beneficiaries of merged banks and register beneficiary with new details on account of change in IFSC / account details. Scheduled payments to such beneficiaries with old details may get failed.   |   Register yourself for Doorstep banking services on 18001037188 / 18001213721 or log on to psbdsb.in and avail the services. Stay Home, Stay Safe.   |   SBI never asks for your Card/PIN/OTP/CVV details on phone, message or email. Please do not click on links received on your email or mobile asking your Bank/Card details.   |   Have you tried our new simplified and intuitive business banking platform? Log in to yonobusiness.sbi to avail business banking services."

c_text = Canvas(c1, bg = "gray68", width = 1600, height = 30, border = 0)
c_text . place(x = 0, y = 400)

text = c_text.create_text(0,-2000, text=moving_text, fill = 'black', tags=("marquee",), anchor='w')
x1,y1,x2,y2 = c_text.bbox("marquee")
width = x2-x1
height = y2-y1

fps = 40
shift()
#Moving Text Ends


"""

Main Page

"""

tk . mainloop()
