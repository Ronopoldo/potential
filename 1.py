import csv

def createCSV(originPath, outPath):
    '''
    Функция для создагния CSV файла, содержащего имя автора и среднего рейтинга всех его книг.
    Также возвращает автора с минимальным рейтингом и его рейтинг (формат для CSV и возвращаемого значений: <authors> - <ratings_authors>)

    Описание аргументов:
    originPath: – Путь к файлу, с которого требуется считать данные
    outPath: – Путь файла, который будет сгенерирован на выходе (*.CSV)
    '''
    originFile = open(originPath, encoding='utf-8').read().split('\n')[1:]

    smallestRating = ['<authors>', 65536]
    ratingObject = {}
    outArray = []
    with open(outPath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['<authors>', '<rating_authors>'])
        for line in originFile:
            tempLine = line.split('%')
            writer.writerow([tempLine[2], tempLine[5]])
            if float(smallestRating[1]) > float((str(tempLine[5]).replace(',','.'))):
                smallestRating = [tempLine[2], (str(tempLine[5]).replace(',','.'))]

    return f'{str(smallestRating[0])} - {str(smallestRating[1])}'

print(createCSV('books.txt', 'books_new.csv'))






