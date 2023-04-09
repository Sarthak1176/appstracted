import pickle

from django.shortcuts import render, redirect


def home(request):
        return render(request, "home.html")

def about(request):
        return render(request, "about.html")

def portfolio(request):
        return render(request, "portfolio.html")

def expertise(request):
        return render(request, "expertise.html")
def adminpanel(request):
        username_list = []
        email_list = []
        message_list = []

        try:
                pickle_in = open("dict.pickle", "rb")
                pickledata = pickle.load(pickle_in)

                for i in pickledata:
                        username_list.append(pickledata[i].get('name'))
                        email_list.append(pickledata[i].get('email'))
                        message_list.append(pickledata[i].get('message'))

                out_list = list(zip(username_list, email_list, message_list))

                request.session["outList"] = out_list

        except:
                print("error occured")

        return render(request, "adminpanel.html",
                      {"out_list":out_list})
def adminlogin(request):



        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')



            if username == "admin":
                    if password == "admin":
                            return redirect('/adminpanel')
                            # return render(request,'adminpanel.html')
                    else:
                            return render(request, "adminlogin.html", {"mymessage": "Please check your password.", "Flag": "True","Navigate": "False"})
            else:
                return render(request, "adminlogin.html", {"mymessage": "Please check your username.", "Flag": "True","Navigate": "False"})


        return render(request, "adminlogin.html")

def contact(request):
        if request.method == "POST":
                customername = request.POST.get('customername')
                customeremail = request.POST.get('customeremail')
                customermessage = request.POST.get('customermessage')

                if customername == "" or customeremail == "" or customermessage == "":
                        return render(request, "contact.html", {
                                "mymessage": "Please complete the form!","Flag": "True", "Navigate": "False"})

                pickledata = {}
                try:
                        pickle_in = open("dict.pickle", "rb")
                        pickledata = pickle.load(pickle_in)
                        print(pickledata)

                except:
                        pass

                pickledata[len(pickledata)+1] = {'name':customername,'email':customeremail,'message':customermessage}
                print(pickledata)
                pickle_out = open("dict.pickle", "wb")
                pickle.dump(pickledata, pickle_out)
                pickle_out.close()

                return render(request, "contact.html", {"mymessage": "Thank you for reaching out to Appstracted. We have received your message and will be in touch within 1-2 Business days.", "Flag": "True", "Navigate": "False"})

        return render(request, "contact.html")