import numpy as np
import pandas as pd


sal = pd.read_csv('Salaries.csv')

print(sal)

print(sal.head())

print(sal.info())

print(sal['BasePay'].mean())

print(sal['OvertimePay'].max())

employeeTitle = sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']
print(employeeTitle)

employee = sal[sal['EmployeeName']=='JOSEPH DRISCOLL']
print(employee['TotalPayBenefits'])

maxSalaryEmp = sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()]
print(maxSalaryEmp)

minSalaryEmp = sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]
print(minSalaryEmp)

meanSalaryByYear = sal.groupby('Year').mean()['BasePay']
print(meanSalaryByYear)

print(sal['JobTitle'].nunique())

print(sal['JobTitle'].value_counts().head(5))

print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1))

print(sal['JobTitle'].apply(lambda x: 'Chief' in x.split()).value_counts())

sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len','TotalPayBenefits']].corr())