import requests
import json

url = 'https://read.douban.com/j/kind/'
data = {"sort":"hot","page":1,"kind":0,"tags":[],"query":"\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    \n    title\n    cover\n    url\n    isBundle\n    coverLabel\n  \n    \n    url\n    title\n  \n    \n    author {\n      name\n      url\n    }\n    origAuthor {\n      name\n      url\n    }\n    translator {\n      name\n      url\n    }\n  \n    \n    abstract\n    editorHighlight\n  \n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: true) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    isNew\n    \n    averageRating\n    ratingCount\n    url\n  \n  \n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n  \n    isInLibrary\n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n  \n        id\n        isOrigin\n      }\n    }\n  ","variables":{}}
headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '1898',
    'Content-Type': 'application/json',
    'Cookie': 'bid=PQmOigG_Wjw; _ga=GA1.3.1170780549.1592903418; _gid=GA1.3.773473832.1592903418; _pk_id.100001.a7dd=3de02629d393da5e.1592903418.1.1592903418.1592903418.; _pk_ses.100001.a7dd=*; _gat=1',
    'Host': 'read.douban.com',
    'Origin': 'https://read.douban.com',
    'Referer': 'https://read.douban.com/category',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'X-CSRF-Token': 'null',
    'X-Requested-With': 'XMLHttpRequest',
}

res = requests.post(url, data=json.dumps(data), headers=headers, verify=False).text
print(res)