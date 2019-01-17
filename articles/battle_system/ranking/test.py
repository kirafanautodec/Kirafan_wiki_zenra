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


def rank(score):
    ranks = {
        'EX':  125,
        'SSS': 120,
        'SS+': 115,
        'SS':  110,
        'S+':  105,
        'S':   100,
        'A+':   95,
        'A':    90,
        'A-':   87,
        'B+':   83,
        'B':    80,
        'B-':   77,
        'C+':   73,
        'C':    70,
        'C-':   67,
        'D+':   63,
        'D':    60
    }
    for rank in ranks:
        if score >= ranks[rank]:
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


with open(mdFileName, 'w') as f:
    f.write('''<!--
title: 最強★５キャラランキング
author: 涙子, 韓湘兒
lang: jp
-->\n\n''')

    f.write(' | '.join([
        'キャラ',
        '武器',
        '進化',
        'ランク'
    ]) + '\n')

    f.write(' | '.join([':---:' for _ in range(4)]) + '\n')

    for item in ranking:
        f.write(' | '.join([
            '<a href="%s">%s</a>' % (
                charaWikiPage % item['CharaID'],
                '<img alt="%s" src="%s" width="64px" />' % (
                    item['CharaID'],
                    charaIconAsset % (str(int(item['CharaID'])+1)))
            ),

            '<a href="%s">%s</a>' % (
                weaponWikiPage % charaToWeapon(item['CharaID']),
                '<img alt="%s" src="%s" width="64px" />' % (
                    charaToWeapon(item['CharaID']),
                    weaponIconAsset % charaToWeapon(item['CharaID']))
            ) if item['Evo'] != '' else '',

            '0' if item['Evo'] == '1' else item['Evo'],

            rank(int(item['Score']))
        ]) + '\n')
