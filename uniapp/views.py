from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from mysql.connector import Error
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.
def display(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def business(request):
    return render(request, 'business.html')


def fourzerofour(request):
    return render(request, '404.html')


def coming_soon(request):
    return render(request, 'coming_soon.html')


def communication(request):
    return render(request, 'communication.html')


def contact(request):
    return render(request, 'contact.html')


def course_details(request):
    return render(request, 'course_details.html')


def faq(request):
    return render(request, 'faq.html')


def form(request):
    return render(request, 'form.html')


def gallery(request):
    return render(request, 'gallery.html')


def language(request):
    return render(request, 'language.html')


def login(request):
    return render(request, 'login.html')


def photography(request):
    return render(request, 'photography.html')


def register(request):
    return render(request, 'register.html')


def single(request):
    return render(request, 'single.html')


def social_media(request):
    return render(request, 'social_media.html')


def software(request):
    return render(request, 'software.html')


def regdetails(request):
    try:
        name = request.POST.get('name')
        username = request.POST.get('email')
        print(username)
        password = request.POST.get('password')
        city = request.POST.get('city')
        mno = int(request.POST.get('mno'))

        conn = mysql.connector.connect(host='localhost', database='registration2', user='root', password='root',
                                       port='3305')
        cursor = conn.cursor()
        query = "insert into login (username, password,role) VALUES ('%s', '%s', '%s')" % (
            username, password, 'Student')
        cursor.execute(query)
        conn.commit()

        id = cursor.lastrowid
        print("last row id", id)

        query1 = "insert into studreg (name, city, mno, lid) VALUES ('%s', '%s', '%d', '%d')" % (name, city, mno, (id))
        cursor.execute(query1)
        conn.commit()


        # return HttpResponse("Data Added..!")
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
    try:
        conn = mysql.connector.connect(host='localhost', database='registration2', user='root', password='root',
                                       auth_plugin='mysql_native_password', port='3305')
        cursor = conn.cursor()

        if request.method == 'POST' and request.FILES['photo']:
            myfile = request.FILES['photo']
            name = request.POST.get('name')

            fs = FileSystemStorage()
            filename = myfile.name
            print("Filename=====", filename)
            extension = filename.split('.')
            print("Extension=====", extension)
            uploaded_file_name = name + "." + extension[1]

            filename = fs.save(uploaded_file_name, myfile)
            print("uploaded_file_name", filename)

            uploaded_file_url = fs.url(filename)
            print("uploaded_file_url", uploaded_file_url)

            query = " INSERT INTO profile (profile, name) VALUES('%s','%s') " % (uploaded_file_url, name )
            cursor.execute(query)
            conn.commit()
            # return HttpResponse("Uploaded..!")

        return render(request, 'login.html')
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def execute(request):
    try:
        username = request.GET.get('username')
        pwsd = request.GET.get('password')

        conn = mysql.connector.connect(host='localhost', database='registration2', user='root', password='root',
                                       port='3305')
        cursor = conn.cursor()
        query = "select lid, role from login where username = '%s' AND password = '%s'" % (username, pwsd)
        cursor.execute(query)
        rows = cursor.fetchone()
        print(rows)
        if rows:
            role = rows[1]
            lid = rows[0]
            request.session['lid'] = lid
            if (role == 'admin'):
                return HttpResponse("Hello Admin")
            elif (role == 'Student'):
                return render(request, 'student.html')
                # return HttpResponse("Hello Student")
            else:
                return HttpResponse("Hello Faculty")
        else:
            return HttpResponse("Enter Valid Username & Password")

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


# def simple_upload(request):

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def recoverpwd(request):
    print("inside")
    username = request.POST.get('username')
    conn = mysql.connector.connect(host='localhost', database='registration2', user='root', password='root',port='3305')
    cursor = conn.cursor()
    query = "select password from login where username = '%s' " % (username)
    cursor.execute(query)
    rows = cursor.fetchone()
    print(rows[0])
    subject = 'Recover Password'
    body = 'Hey yash, your password is: '+ (rows[0])
    to1 = [username]
    email = EmailMessage(subject, body, to=to1)
    email.send()
    return render(request,'message.html')

def index(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='registration2', user='root', password='root', port='3305')
        cursor = conn.cursor()
        query = "select * from country"
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        return render(request, 'register.html', {'country':rows})
    except Error as e:
       print(e)
    finally:
       cursor.close()
       conn.close()


def getcity(request):
    try:
        id = int(request.GET.get('state'))

        conn = mysql.connector.connect(host='localhost', database='registration2', user='root', password='root', port='3305')
        cursor = conn.cursor()
        query = "select * from city where sid= '%d'" %(id)
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)

        return render(request, 'register.html', {'city':rows})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def getstate(request):
    id = int(request.GET.get('country'))

    conn = mysql.connector.connect(host='localhost', database='registration2', user='root', password='root',
                                   port='3305')
    cursor = conn.cursor()
    query = "select * from statetable where countryid= '%d'" % (id)
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render(request, 'register.html', {'state': rows})

'''def prediction(request):
    return render(request, 'predictionpage.html')
'''
def prediction2(request):
    return render(request, 'predictionpage2.html')

def getprediction(request):
    uniname= request.POST.get('uniname')
    gre= int(request.POST.get('gre'))
    ielts = int(request.POST.get('ielts'))
    cgpa = int(request.POST.get('cgpa'))

    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    from sklearn.ensemble import RandomForestClassifier
    import win32api

    uni = pd.read_csv('C:/Users/Shaurya/PycharmProjects/UniversityAdmission/templates/universitydata2.csv')
    X = uni[['uid','GRE', 'IELTS', 'Percentage']]
    y = uni['Y/N']
    print('hello')
    uid= uni.loc[uni['Universityname']==uniname]['uid']
    #uid= uid[0]
    print(uid)

    uid= np.array(uid)
    uid= uid[0]
    print(uid)

    X_train, X_test, y_train, y_test= train_test_split(X,y, test_size= 0.2, random_state= 0)

    from sklearn.preprocessing import MinMaxScaler

    obj = MinMaxScaler()
    # Scaling down both train and test data set
    X_train = obj.fit_transform(X_train)
    X_test = obj.fit_transform(X_test)

    #regressor= LogisticRegression(random_state=0)
    #regressor.fit(X_train, y_train)

    regressor= RandomForestClassifier(n_estimators= 20, criterion= 'entropy', random_state=0)
    regressor.fit(X_train, y_train)

    y_pred= regressor.predict(X_test)
    y_pred= np.rint(y_pred)

    X1_test= np.array([uid,gre,ielts,cgpa])
    X1_test = obj.fit_transform(X1_test.reshape(4,1))

    X1_test= X1_test.reshape(1,4)
    y1_pred= regressor.predict(X1_test)
    y1_pred= np.rint(y1_pred)
    print(y1_pred)

    from sklearn.metrics import confusion_matrix
    cm= confusion_matrix(y_test,y_pred)
    print(cm)

    if y1_pred == 0:
        s = "Sorry there are little chances for your admit"
        win32api.MessageBox(0,s)
        return render(request,'predictionpage2.html',{'s':s})

    elif y1_pred == 1:
        s = "Congratulations you may apply to this university"
        win32api.MessageBox(0, s)
        return render(request, 'predictionpage2.html', {'s': s})
    else:
        s = "in else part"
        win32api.MessageBox(0, s)
        return render(request, 'predictionpage2.html', {'s': s})


    print(accuracy_score(y_test,y_pred))
    #print(regressor.score(X,y))
    #p = accuracy_score(y_test, y_pred)


    #return render(request,'predictionpage.html',{'prediction':y1_pred})
    #return render(request,'predictionpage.html',{'p':p})



