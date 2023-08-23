import customtkinter

customtkinter.set_appearance_mode('light')

app = customtkinter.CTk()
app.geometry('360x370')
app.title('Calculator')
def calcular():
    calcuator = output.get('0.0', 'end')
    result = eval(calcuator)
    output.delete('0.0', 'end')
    output.insert('0.0', result)
FontApp = ('Poppins',20,'bold')

output = customtkinter.CTkTextbox(app, width=340, height=60,corner_radius=10, border_width=2, border_color='#3F4143', font=FontApp)
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)


button_1 = customtkinter.CTkButton(app,text='1', command= lambda:output.insert('end', 1), corner_radius=10, width=80, height=55, font=FontApp)
button_1.grid(row=1, column=0, padx=5, pady=5)


button_2 = customtkinter.CTkButton(app,text='2', command= lambda:output.insert('end', 2), corner_radius=10, width=80, height=55, font=FontApp)
button_2.grid(row=1, column=1, padx=5, pady=5)


button_3 = customtkinter.CTkButton(app,text='3', command=lambda:output.insert('end', 3), corner_radius=10, width=80, height=55, font=FontApp)
button_3.grid(row=1, column=2, padx=5, pady=5)


button_4 = customtkinter.CTkButton(app,text='4', command=lambda:output.insert('end', 4), corner_radius=10, width=80, height=55, font=FontApp)
button_4.grid(row=2, column=0, padx=5, pady=5)


button_5 = customtkinter.CTkButton(app,text='5', command=lambda:output.insert('end', 5), corner_radius=10, width=80, height=55, font=FontApp)
button_5.grid(row=2, column=1, padx=5, pady=5)


button_6 = customtkinter.CTkButton(app,text='6', command=lambda:output.insert('end', 6), corner_radius=10, width=80, height=55, font=FontApp)
button_6.grid(row=2, column=2, padx=5, pady=5)


button_7 = customtkinter.CTkButton(app,text='7', command=lambda:output.insert('end', 7), corner_radius=10, width=80, height=55, font=FontApp)
button_7.grid(row=3, column=0, padx=5, pady=5)


button_8 = customtkinter.CTkButton(app,text='8', command=lambda:output.insert('end', 8), corner_radius=10, width=80, height=55, font=FontApp)
button_8.grid(row=3, column=1, padx=5, pady=5)


button_9 = customtkinter.CTkButton(app,text='9', command=lambda:output.insert('end', 9), corner_radius=10, width=80, height=55, font=FontApp)
button_9.grid(row=3, column=2, padx=5, pady=5)


button_0 = customtkinter.CTkButton(app, text='0', command= lambda:output.insert('end', 0) , corner_radius=10, width=80, height=55, font=FontApp)
button_0.grid(row=4, column=0, padx=5, pady=5)


button_delete = customtkinter.CTkButton(app,text='Clear', command=lambda:output.delete('0.0', 'end'), corner_radius=10, width=80, height=55, font=FontApp)
button_delete.grid(row=4, column=1, padx=5, pady=5)


button_calculator = customtkinter.CTkButton(app,text='=', command=calcular, corner_radius=10, width=80, height=55, font=FontApp)
button_calculator.grid(row=4, column=2, padx=5, pady=5)


button_sum = customtkinter.CTkButton(app,text='+', command=lambda:output.insert('end', '+'),fg_color="#EA5738",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=FontApp)
button_sum.grid(row=1, column=3, padx=5, pady=5)


button_s = customtkinter.CTkButton(app,text='-', command=lambda:output.insert('end', '-'),fg_color="#EA5738",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=FontApp)
button_s.grid(row=2, column=3, padx=5, pady=5)


btn_multip = customtkinter.CTkButton(app,text='x', command=lambda:output.insert('end', '*'),fg_color="#EA5738",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=FontApp)
btn_multip.grid(row=3, column=3, padx=5, pady=5)


button_divide = customtkinter.CTkButton(app,text='/', command=lambda:output.insert('end', '*'),fg_color="#EA5738",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=FontApp)
button_divide.grid(row=4, column=3, padx=5, pady=5)

app.mainloop()