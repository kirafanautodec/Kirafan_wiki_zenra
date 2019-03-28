import csv


def csvLoad(csvFileName):
    ans = []
    with open(csvFileName) as csvFile:
        csvReader = csv.reader(csvFile)
        header = next(csvReader)
        for row in csvReader:
            item = {}
            for i in range(len(header)):
                item[header[i]] = row[i]
            ans.append(item)
    return ans


ranks = {
    'EX':   {'score': 125, 'note': ''},
    'SSS+': {'score': 122, 'note': ''},
    'SSS':  {'score': 120, 'note': ''},
    'SS+':  {'score': 115, 'note': ''},
    'SS':   {'score': 110, 'note': ''},
    'SS-':  {'score': 108, 'note': ''},
    'S+':   {'score': 105, 'note': ''},
    'S':    {'score': 100, 'note': ''},
    'A+':   {'score':  95, 'note': 'メリー（専用武器４）は<br />眠り免疫の敵に対してランクが A- で<br />眠り免疫でない敵に対しては EX です'},
    'A':    {'score':  90, 'note': ''},
    'A-':   {'score':  87, 'note': ''},
    'B+':   {'score':  83, 'note': ''},
    'B':    {'score':  80, 'note': ''},
    'B-':   {'score':  77, 'note': ''},
    'C+':   {'score':  73, 'note': ''},
    'C':    {'score':  70, 'note': ''},
    'C-':   {'score':  67, 'note': ''},
    'D+':   {'score':  63, 'note': ''},
    'D':    {'score':  60, 'note': ''}
}


def rank(score):
    for rank in ranks:
        if score >= ranks[rank]['score']:
            return rank
    return '?'


def charaToWeapon(charaID):
    charaID = str(charaID)
    return charaID[:5] + charaID[6] + '0'


csvFileName = "ranking.csv"
mdFileName = "article_jp.md"
charaIconAsset = "/static/assets/texture/charauiresource/mergedcharaicon/charaicon_%s.jpeg"
weaponIconAsset = "/static/assets/texture/weaponicon/weaponicon_wpn_%s.png"
charaWikiPage = "/chara/%s"
weaponWikiPage = "/weapon/%s"

ranking = csvLoad(csvFileName)
line = 6
lineCount = 0
rankCurrent = None

head = '''\
<!--
title: 最強★５キャラランキング
author: 佐天涙子, 韓湘兒
lang: jp
-->
'''

with open(mdFileName, 'w') as f:
    f.write(head + '\n')

    for item in ranking:
        if rankCurrent != rank(int(item['Score'])):
            if rankCurrent is not None:
                if lineCount != line:
                    f.write(' | ')
                f.write('\n<small>' + ranks[rankCurrent]['note'] + '</small>\n')

            rankCurrent = rank(int(item['Score']))

            f.write(' | '.join([rankCurrent] + [' - ' for _ in range(line - 1)]) + '\n')
            f.write(' | '.join([':---:' for _ in range(line)]) + '\n')
            lineCount = 0

        cellCount = 1 if item['Evo'] == '' else 2

        if lineCount + cellCount > line:
            f.write('\n')
            lineCount = 0

        if lineCount != 0:
            f.write(' | ')

        lineCount += cellCount

        f.write(
            '<a href="%s">%s</a>' % (
                charaWikiPage % item['CharaID'],
                '<img alt="%s" src="%s" width="64px" />' % (
                    item['CharaID'],
                    charaIconAsset % (str(int(item['CharaID'])+1)))))

        if item['Evo'] == '': continue

        f.write(' | ')

        f.write(
            '<a href="%s">%s</a> %s' % (
                weaponWikiPage % charaToWeapon(item['CharaID']),
                '<img alt="%s" src="%s" width="64px" />' % (
                    charaToWeapon(item['CharaID']),
                    weaponIconAsset % charaToWeapon(item['CharaID'])),
                item['Evo'] if item['Evo'] != '1' else ''))
