from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
from tkinter.scrolledtext import *
import numpy as np
import matplotlib.pyplot as plt
from requests import *




root = Tk()
root.title("EMS")
root.geometry("800x500+50+50")
root.configure(bg='light green')
f = ("Century", 24, "bold")

def add():
	add_window = Toplevel(root)
	root.withdraw()
	add_window.deiconify()
	add_window.title("ADD")
	add_window.geometry("800x500+50+50")
	f=("arial",20,"bold")
	add_window.configure(bg='light blue')

	a_lb_id=Label(add_window,text="  Enter id: ",font=f)
	a_ent_id=Entry(add_window,font=f)
	a_lb_name=Label(add_window,text="  Enter name: ",font=f)
	a_ent_name=Entry(add_window,font=f)
	a_lb_salary=Label(add_window,text="  Enter salary: ",font=f)
	a_ent_salary=Entry(add_window,font=f)

	a_lb_id.pack(pady=5)
	a_ent_id.pack(pady=5)
	a_lb_name.pack(pady=5)
	a_ent_name.pack(pady=5)
	a_lb_salary.pack(pady=5)
	a_ent_salary.pack(pady=5)
	
	def save():
		try:
			id=a_ent_id.get()
			if not id.isdigit():
				showerror("Issue","ID should be numbers only ")
				a_ent_id.delete(0,END)
				a_ent_id.focus()
			if id == "0":
				showerror("Issue","id cannot be zero")
				a_ent_id.delete(0,END)
				a_ent_id.focus()
			if id==" ":
				showerror("Issue","id cannot be empty ")
				a_ent_id.delete(0,END)
				a_ent_id.focus()

			name=a_ent_name.get()

			if not name.isalpha():
				showerror("Issue","name should be alphabets only")
				a_ent_name.delete(0,END)
				a_ent_name.focus()
			if name==" ":
				showerror("Issue","name cannot be empty")
				a_ent_name.delete(0,END)
				a_ent_name.focus()
			if len(name.strip())<2:
				showerror("Issue","name should be min 2 letters")
				a_ent_name.delete(0,END)
				a_ent_name.focus()

			salary=float(a_ent_salary.get())
			if salary<=0:
				showerror("Issue","salary cannot be 0 or less than 0")
				a_ent_salary.delete(0,END)
				a_ent_salary.focus()
			if salary==" ":
				showerror("Issue","SALARY	 cannot be empty")
				a_ent_salary.delete(0,END)
				a_ent_salary.focus()
			if not a_ent_salary.get().isdigit():
				showerror("Issue","numbers only")
				a_ent_salary.delete(0,END)
				a_ent_salary.focus()

			else:
				con=None
				try:
					con = connect("ems.db")
					cursor = con.cursor()
					sql = "insert into customers values(?,?,?)"
					data = (id, name, salary)
					cursor.execute(sql, data)
					con.commit()
					showinfo("Succes", "Thanks ")
					a_ent_id.delete(0,END)
					a_ent_name.delete(0,END)
					a_ent_salary.delete(0,END)
					a_ent_id.focus()
				
				except Exception as e:
					con.rollback()
					showerror("issue ", e)
				finally:
					if con is not None:
						con.close()

		except Exception as e:
			showerror("Issue ", e)

	def back():
		add_window.withdraw()
		root.deiconify()

	a_bt_save=Button(add_window,text="Save",font=f,command=save)
	a_bt_back=Button(add_window,text="Back",font=f,command=back)
	a_bt_save.pack(pady=5)
	a_bt_back.pack(pady=5)

	add_window.mainloop()

def view():
	view_window=Toplevel(root)
	root.withdraw()
	view_window.deiconify()
	view_window.title("View")
	view_window.geometry("800x500+50+50")
	f=("arial",20,"bold")
	view_window.configure(bg="coral2")
	vst=ScrolledText(view_window,font=f,height=10,width=40)
	vst.pack(pady=20)
	try:
		con = connect("ems.db")
		cursor = con.cursor()
		sql = "select * from customers"
		cursor.execute(sql)
		data = cursor.fetchall()
		info=""
		for d in data :
			info =info+" id - "+str(d[0])+ "|  name - "+str(d[1])+"| salary - "+str(d[2])+"\n"
		vst.insert(INSERT,info)
		con.commit()

		

	except Exception as e:
		showerror("Issue", e)

	finally:
		if con is not None:
			con.close()

	
	def back():
		view_window.withdraw()
		root.deiconify()


	v_bt_back=Button(view_window,text="Back",font=f,command=back)
	v_bt_back.pack(pady=10)

	view_window.mainloop()

def update():
	update_window = Toplevel(root)
	root.withdraw()
	update_window.deiconify()
	update_window.title("Update")
	update_window.geometry("800x500+50+50")
	f=("arial",20,"bold")
	update_window.configure(bg='goldenrod1')

	u_lb_id=Label(update_window,text="  Enter id: ",font=f)
	u_ent_id=Entry(update_window,font=f)
	u_lb_name=Label(update_window,text="  Enter name: ",font=f)
	u_ent_name=Entry(update_window,font=f)
	u_lb_salary=Label(update_window,text="  Enter salary: ",font=f)
	u_ent_salary=Entry(update_window,font=f)

	u_lb_id.pack(pady=5)
	u_ent_id.pack(pady=5)
	u_lb_name.pack(pady=5)
	u_ent_name.pack(pady=5)
	u_lb_salary.pack(pady=5)
	u_ent_salary.pack(pady=5)

	def update1():
		try:
			uname = u_ent_name.get()
			if len(uname.strip()) < 2:
				showerror("Invalid Input","name should be min 2 letters")
				u_ent_name.delete(0,END)
				u_ent_name.focus()
				

			if not uname.isalpha():
				showerror("Invalid Input","name should contain alpha only")
				u_ent_name.delete(0,END)
				u_ent_name.focus()

			

			
			uid = u_ent_id.get()
			if not uid.isdigit():
				showerror("Invalid Input","id should be numbers only")
				u_ent_id.delete(0,END)
				u_ent_id.focus()

			usalary = float(u_ent_salary.get())
			

			if usalary < 0 or usalary > 999999999:
				showerror("Invalid Input","enter valid salary")
				u_ent_salary.delete(0,END)
				u_ent_salary.focus()

			else:
				con = None
				try:
					con = connect("ems.db")
					cursor = con.cursor()
					
					sql = """
						UPDATE customers
						SET name = ?, salary = ?
						WHERE id =?
					"""
					data = (uname, usalary, uid)
					cursor.execute(sql, data)
					if cursor.rowcount == 1:
						con.commit()
						showinfo("Updated", "enquiry Updated")
					else:
						showinfo("Invalid","Record does not exist")
					
					u_ent_id.delete(0,END)
					u_ent_name.delete(0,END)
					u_ent_salary.delete(0,END)
					
					u_ent_id.focus()
				
				except Exception as e:
					con.rollback()
					showerror("issue ", e)
				finally:
					if con is not None:
						con.close()	

		
		except Exception as e:
			showerror("Issue", e)

	def back():
		update_window.withdraw()
		root.deiconify()

	u_bt_update=Button(update_window,text="Update",font=f,command=update1)
	u_bt_back=Button(update_window,text="Back",font=f,command=back)
	u_bt_update.pack(pady=5)
	u_bt_back.pack(pady=5)

	update_window.mainloop()

def delete():
	delete_window = Toplevel(root)
	root.withdraw()
	delete_window.deiconify()
	delete_window.title("Update")
	delete_window.geometry("800x500+50+50")
	f=("arial",20,"bold")
	delete_window.configure(bg='lightslateblue')

	d_lb_id=Label(delete_window,text="  Enter id: ",font=f)
	d_ent_id=Entry(delete_window,font=f)

	d_lb_id.pack(pady=20)
	d_ent_id.pack(pady=20)

	def delete1():
		con = None
		try:
			con = connect("ems.db")
			cursor = con.cursor()
			deln = int(d_ent_id.get())
			sql = "delete from customers where id='%d'"
			cursor.execute(sql % (deln))
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Deleted", "enquiry deleted")
				d_ent_id.delete(0,END)
			else:
				showinfo("Invalid","Record does not exist")
				d_ent_id.delete(0,END)
		except Exception as e:
			con.rollback()
			showerror("issue", e)
		finally:
			if con is not None:
				con.close()

	def back():
		delete_window.withdraw()
		root.deiconify()

	d_bt_delete=Button(delete_window,text="Delete",font=f,command=delete1)
	d_bt_back=Button(delete_window,text="Back",font=f,command=back)
	d_bt_delete.pack(pady=10)
	d_bt_back.pack(pady=10)



	delete_window.mainloop()

def chart():
	try:
		con = connect("ems.db")
		cursor = con.cursor()
		sql = "select * from customers order by salary desc limit 5"
		cursor.execute(sql)
		data = cursor.fetchall()
		names = np.array([])
		salaries = np.array([])
		for d in data:
			names = np.append(names, [str(d[1])])
			salaries = np.append(salaries, [float(d[2])])
		plt.bar(names,salaries,width = 0.4,color=["red","green","blue"])
		plt.xlabel("Employee Name")
		plt.ylabel("Salary")
		plt.title("Top 5 Salaried Employees")
		plt.show()
	except Exception as e:
		showerror("Error",e)

bt_add= Button(root,text="  Add ",font=f,width =7,height=1,command =add)
bt_view= Button(root,text=" View ",font=f,width =7,height=1,command=view)
bt_update= Button(root,text="Update",font=f,width =7,height=1,command=update)
bt_delete= Button(root,text="Delete",font=f,width =7,height=1,command=delete)
bt_chart= Button(root,text="Charts",font=f,width =7,height=1,command=chart)

bt_add.pack()
bt_view.pack()
bt_update.pack()
bt_delete.pack()
bt_chart.pack()

lb_loc=Label(root,text="   Location   :",font=f)
lb_temp=Label(root,text="Temperature:",font=f)
ent_loc=Entry(root,font=f)
ent_temp=Entry(root,font=f)

url="https://ipinfo.io/"
res=get(url)
if res.status_code == 200:
    data=res.json()
    state=data["region"]
    ent_loc.insert(0,state)

else:
    ent_loc.insert(0,"cant connect")

ent_temp.insert(0,"35 °C")

lb_loc.place(x=50,y=350)
lb_temp.place(x=50,y=400)
ent_loc.place(x=350,y=350)
ent_temp.place(x=350,y=400)

def on_closing():
	if askyesno("Quit", "Are u sure u want to exit"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

