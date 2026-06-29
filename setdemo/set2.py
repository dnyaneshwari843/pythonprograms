cricket={"dnyanu","sana","kanchan","snehal"}
football={"dnyanu","sana","kaveri","priya"}
basketball={"dnyanu","ka","piyu","swara"}
all=cricket&football&basketball
print("the student playing all three games",all)
all1=cricket-football-basketball
print("the student only playing cricket",all1)
cf=cricket&football
notp=cf-basketball
print("the student only playing cricket and football",notp)
set=cricket|basketball|football
notbasket=set-basketball
print(" student not playing basketball",notbasket)

