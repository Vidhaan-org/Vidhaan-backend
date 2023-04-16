# Vidhaan-backend




# Query

![image](https://user-images.githubusercontent.com/65972077/185349854-d4326db1-f302-40ad-a013-9f803bd16dd4.png)


**Feilds**


```python
class CaseType(DjangoObjectType):
    class Meta:
        model = Case
        fields = '__all__'

class LawerType(DjangoObjectType):
    class Meta:
        model = Advocate
        fields = ('advocate_name', 'advocate_number')

class JudgeType(DjangoObjectType):
    class Meta:
        model = Judge
        fields = ('judge_name', 'judge_number')
class PetitionerType(DjangoObjectType):
    class Meta:
        model = Petitioner
        fields = ('id','petitioner_type', 'petitioner_name')
      
class PetitionsList(DjangoObjectType):
    class Meta:
        model = Petition
        fields = '__all__'

class ActType(DjangoObjectType):
    class Meta:
        model = Act
        fields = '__all__'

class TrackCaseList(DjangoObjectType):
    class Meta:
        model = TrackCases
        fields = ('action_status','action_date','case_id')
```
    
    
**Example 1**

```graphql
query{
  cases{
    id
    fillingNumber
    caseType
  }
}
```

**output**

```json
{
  "data": {
    "cases": [
      {
        "id": "1",
        "fillingNumber": 1,
        "caseType": "CIVIL_MISCELLEANOUS_APPEAL"
      },
      {
        "id": "2",
        "fillingNumber": 12,
        "caseType": "CIVIL_MISCELLEANOUS_APPEAL"
      }
    ]
  }
}
```

**Example 2** - nested map

```graphql
query{
  petitionFile{
    id
    caseType
    petitioner{
      petitionerName
      id
    }
  }
}
```

**output**

```json
{
   "data": {
    "petitionFile": [
      {
        "id": "1",
        "caseType": "CIVIL_MISCELLEANOUS_APPEAL",
        "petitioner": [
          {
            "petitionerName": null,
            "id": "1"
          }
        ]
      },
      {
        "id": "2",
        "caseType": null,
        "petitioner": []
      },
      {
        "id": "3",
        "caseType": null,
        "petitioner": []
      },
      {
        "id": "4",
        "caseType": "CIVIL_MISCELLEANOUS_APPEAL",
        "petitioner": []
      },
      {
        "id": "5",
        "caseType": "CIVIL_MISCELLEANOUS_APPEAL",
        "petitioner": []
      },
      {
        "id": "6",
        "caseType": null,
        "petitioner": []
      },
      {
        "id": "7",
        "caseType": null,
        "petitioner": []
      }
    ]
  }
}
```



