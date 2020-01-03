from robobrowser import RoboBrowser
import requests

#######################################################################
## Usage Example                                                      #
#                                                                     #
# import Browse as br                                                 #
#                                                                     #
# name = ''                                                           #
# psw = ''                                                            #
#                                                                     #
# problem_code = 'EVIPRO'                                             #
# contest_name = ''                                                   #
# file_loc = 'sol.cpp'                                                #
#                                                                     #
# br.submit_solution(name, psw, problem_code, file_loc, contest_name) #
#                                                                     #
#######################################################################

def submit_solution(usern, psw, problem_code, file_loc, contest_name=""):
    Init()
    if Login(usern, psw) == -1:
        return 'Session limit reched'
    Submit(problem_code, file_loc, contest_name)
    Logout()


def Init():
    global newSession,browser,loginStatus,url
    newSession = requests.session()
    newSession.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    browser = RoboBrowser(history = True, session = newSession,parser = 'html.parser')
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

    session_limit_form = browser.get_form(id = 'session-limit-page')
    if session_limit_form is not None:
        print('Session limit reached.. Please logout and try again')
        return -1

    return 1




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

    # if(loginStatus == 0):
    #     raise RuntimeError 'Not logged in'

    submit_url = url
    if(contest_name!=""):
        submit_url+=contest_name+'/'
    submit_url+='submit/'+problem_code


    browser.open(submit_url)
    submission_form = browser.get_form(id = 'problem-submission')

    if submission_form is None:
        temp_form = browser.get_form(id = 'do-not-show-ide-on-submit-form')
        if temp_form is None:
            Logout()
            return 'Problem Code  or Contest doesn\'t exist'
        browser.submit_form(temp_form)
        submission_form = browser.get_form(id = 'problem-submission')


    submission_form['files[sourcefile]'].value = open(file_loc,'rb')
    submission_form['language']='44'
    browser.submit_form(submission_form)
    return 'Solution submitted to '+problem_code

    # with open("subres.html", "w",encoding="utf-8") as text_file:
    #     print(str(browser.select), file=text_file)
