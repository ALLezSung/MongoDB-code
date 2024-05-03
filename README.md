### MongoDB操作

##### 2024-04-30

---

###### ①了解py的csv库, pandas库, 尝试将查询获得的数据生成.csv文件

测试使用集合：

```json
[
  {
    _id: ObjectId('6627462c5f725acd29117b7c'),
    name: 'Jack',
    belong: '404'
  },
  {
    _id: ObjectId('6627462c5f725acd29117b7d'),
    name: 'Pony',
    belong: '404'
  },
  {
    _id: ObjectId('6627462c5f725acd29117b7e'),
    name: 'Elon',
    belong: '404'
  },
  {
    _id: ObjectId('66274a745f725acd29117b80'),
    name: 'Ma',
    belong: '505'
  },
  {
    _id: ObjectId('66274a745f725acd29117b81'),
    name: 'Yun',
    belong: '505'
  },
  {
    _id: ObjectId('66274a745f725acd29117b82'),
    name: 'Musk',
    belong: '505'
  },
  {
    _id: ObjectId('66278de05f725acd29117b83'),
    name: '张三',
    phone: '13888888888',
    belong: '10086000000'
  },
  {
    _id: ObjectId('66278de05f725acd29117b84'),
    name: '李四',
    phone: '13888888889',
    belong: '10086000000'
  },
  {
    _id: ObjectId('66278de05f725acd29117b85'),
    name: '王五',
    phone: '13888888880',
    belong: '10086000000'
  },
  {
    _id: ObjectId('66278de05f725acd29117b86'),
    name: '赵六',
    phone: '1311111111',
    belong: '13155555555'
  }
]
```

测试结果：

```python
#    collection = 'identity'
#    filter = {}
#    projection = {"_id":0, "name":1, "belong":1}

name,belong
Jack,404
Pony,404
Elon,404
Ma,505
Yun,505
Musk,505
张三,10086000000
李四,10086000000
王五,10086000000
赵六,13155555555

```

