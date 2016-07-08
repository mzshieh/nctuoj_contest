from include import include
import config
import os
class Handler:
    pass
include(Handler, "./handler/")
urls = [
    ('/', Handler.Index),
    ('/api/contest/', Handler.api.Contest),
    ('/api/languages/', Handler.api.Languages),
    ('/api/users/', Handler.api.Users),
    ('/api/users/(\d+)/', Handler.api.User),
    ('/api/users/me/', Handler.api.UsersMe),
    ('/api/users/upload/', Handler.api.UserUpload),
    ('/api/users/code/', Handler.api.UsersCode, {'path': '/tmp'}),
    ('/api/users/csv/', Handler.api.UsersCSV),
    ('/api/users/signin/', Handler.api.UserSignIn),
    ('/api/problems/', Handler.api.Problems),
    ('/api/problems/meta/', Handler.api.ProblemsMeta),
    ('/api/problems/(\d+)/', Handler.api.Problem),
    ('/api/problems/(\d+)/pdf/', Handler.api.ProblemPdf, {'path': os.path.join(config.DATA_ROOT, 'data/problems')}),
    ('/api/problems/(\d+)/meta/', Handler.api.ProblemMeta),
    ('/api/problems/(\d+)/executes/', Handler.api.ProblemExecutes),
    #('/api/problems/(\d+)/rejudge/', Handler.api.ProblemRejudge),
    ('/api/problems/(\d+)/testdata/', Handler.api.Testdata),
    ('/api/problems/(\d+)/testdata/(\d+)/', Handler.api.Testdatum),
    ('/api/problems/(\d+)/testdata/(\d+)/(\w+)/', Handler.api.TestdatumFile, {'path': os.path.join(config.DATA_ROOT, 'data/testdata')}),
    ('/api/problems/(\d+)/verdict/', Handler.api.ProblemVerdict),
    ('/api/problems/(\d+)/verdict/file/', Handler.api.ProblemVerdictFile, {'path': os.path.join(config.DATA_ROOT, 'data/verdicts')}),
    ('/api/submissions/', Handler.api.Submissions),
    ('/api/submissions/(\d+)/', Handler.api.Submission),
    ('/api/submissions/(\d+)/file/', Handler.api.SubmissionFile, {'path': os.path.join(config.DATA_ROOT, 'data/submissions')}),
    #('/api/submissions/(\d+)/rejudge/', Handler.api.SubmissionRejudge),
    ('/api/clarifications/', Handler.api.Clarifications),
    ('/api/clarifications/(\d+)/', Handler.api.Clarification),
    ('/api/executes/', Handler.api.Executes),
    ('/api/executes/(\d+)/', Handler.api.Execute),
    ('/api/verdicts/', Handler.api.Verdicts),
    ('/api/system/(\w*)/', Handler.api.System),
    ('/api/system/', Handler.api.System),
    ('/api/scoreboard/', Handler.api.Scoreboard),
    ('/api/judge/', Handler.api.JudgeSubmission),
    ('/api/judge/testdata/', Handler.api.JudgeSubmissionTestdata),
]
