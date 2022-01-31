import csv
import plotly_express as px
import pandas as pd

read=pd.read_csv("data107.csv")
student_id=read.groupby(["student_id","level"], as_index=False)["attempt"].mean()
fig=px.scatter(student_id,x="student_id",y="level",color="attempt",size="attempt")
fig.show()