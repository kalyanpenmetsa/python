import nltk
#from textblob import TextBlob
import jenkins, random

# inp = input('Enter a sentence: ')
# analysis = TextBlob(inp)
# print(analysis.translate(to='es'))

###############
ci_jenkins_url = "http://localhost:8080"
username = 'kayvee29'
token = "59524f57eb165a3a088c39d7819fe272"
j = jenkins.Jenkins(ci_jenkins_url, username=username, password=token)
###############
yes = ['yes','y','ya','yep','yo','yeah']
no = ['no','n','na','nope','nada']
foo = ['There is no job specified in your request!','Are you nuts?','You are a piece of work, arent you?','Go to hell']
inp = input('Hey, what are you looking for?\n')
tokens = nltk.word_tokenize(inp)
Env = ['t1','t2','t3','t4','t5','t6','test1','test2','test3','test4']
def whichEnv(token):
    return [i for i in tokens if i.lower() in Env]

def whichRel(token):
    return [i for i in token if i.isdigit()]
    # return re.findall(r'\b\d+\b', token)

def getJobList(JInstance):
    jobs = JInstance.get_jobs()
    job_list = []
    for c,i in enumerate(jobs):
        job_list.append(jobs[c]['fullname'])
    return job_list

def whichJob(j,token):
    return [i for i in token if i.upper() in getJobList(j)]

#print(whichJob(j,tokens))

#print(whichEnv(tokens)[0])
#print(whichRel(tokens)[0])

# if len(whichEnv(tokens))>1 or len(whichRel(tokens))>1 or len(whichJob(j,tokens))>1 or len(whichEnv(tokens))<1 or len(whichRel(tokens))<1 or len(whichJob(j,tokens))<1:
if len(whichEnv(tokens))==1 and len(whichRel(tokens))==1 and len(whichJob(j,tokens))==1:

    inp2 = input('Are you sure you want to run %s build with %s code in %s?\n' %(whichJob(j,tokens)[0],whichRel(tokens)[0],whichEnv(tokens)[0]))
    if inp2.lower() in yes:
        print('Alright, lets do this!')
        parameters = {'RELEASE': whichRel(tokens)[0], 'ENVIRONMENT': whichEnv(tokens)[0]}
        j = jenkins.Jenkins(ci_jenkins_url, username=username, password=token)
        j.build_job(whichJob(j,tokens)[0], parameters)

    elif inp2.lower() in no:
        print('Okay, whatever!')
else:
    print(random.choice(foo))
