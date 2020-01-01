from robobrowser import RoboBrowser
import requests
# import Login,Logout,Submit

################################################
## Example

# name = ''
# psw = ''
#
# problem_code = 'EVIPRO'
#
# br.Init()
# br.Login(name,psw)
# br.Submit(problem_code, 'sol.cpp')
# br.Logout()
#################################################


def Init():
    global newSession,browser,loginStatus,url
    newSession = requests.session()
    newSession.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    browser = RoboBrowser(history = True,session=newSession)
    loginStatus = 0
    url = 'https://www.codechef.com/'



## Login
def Login(usern, psw):
    global newSession,browser,loginStatus,url
    if(loginStatus == 1):
        return

    browser.open(url)

    login_form = browser.get_form(id='new-login-form')

    login_form['name'].value = usern
    login_form['pass'].value = psw

    login_form.serialize()

    browser.submit_form(login_form)
    loginStatus = 1

    # Add session limit funcitonality later



##
## Logout

def Logout():
    global newSession,browser,loginStatus,url
    if(loginStatus == 0):
        return

    browser.open(url+'logout')
    loginStatus = 0




##Submit

def Submit(problem_code, file_loc, contest_name=""):
    global newSession,browser,loginStatus,url
    submit_url = url
    if(contest_name!=""):
        submit_url+=contest_name+'/'
    submit_url+='submit/'+problem_code

    browser.open(submit_url)

    with open("subres.html", "w",encoding="utf-8") as text_file:
        print(str(browser.select), file=text_file)

    submission_form = browser.get_form(id = 'problem-submission')

    if submission_form is None:
        temp_form = browser.get_form(id = 'do-not-show-ide-on-submit-form')

        ## Double check
        # if temp_form is None:
        #     print('tempform is none, returning')
        #     return


        browser.submit_form(temp_form)

        submission_form = browser.get_form(id = 'problem-submission')


    submission_form['files[sourcefile]'].value = open(file_loc,'rb')
    browser.submit_form(submission_form)
    print('Solution submitted to '+problem_code)

    # with open("subres.html", "w",encoding="utf-8") as text_file:
    #     print(str(browser.select), file=text_file)
