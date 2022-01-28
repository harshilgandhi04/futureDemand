import requests
import bs4
import psycopg2

try:
    #Establishing the connection with PostgreSql
    conn = psycopg2.connect(
        database="postgres",
        user='postgres',
        password='Qwerty@12345',
        host='db',
        port= '5432'
        )

    cursor = conn.cursor()

    #Make a request to webpage and store the html response
    res = requests.get('https://www.lucernefestival.ch/en/program/summer-festival-22')

    #Convert request type object to BS Object and parse as lxml
    soupObj = bs4.BeautifulSoup(res.text,'lxml')

    #Extract events 
    eventsList = soupObj.select('div[id^="event_id_"]')

#     create_eventsMetadata_query = """ CREATE TABLE IF NOT EXISTS EventsMetadata(
#         Event_Id  BIGINT NOT NULL  ,
#         Title     VARCHAR(100) NULL,
#         Artists   VARCHAR(100) NULL,
#         Works     VARCHAR(100) NULL,
#         ImageLink VARCHAR(500) NULL,
#         Location  VARCHAR(100) NULL,
#         EventDate DATE NULL        ,
#         EventTime VARCHAR(50) NULL ,
#         CreatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
#         """
#     cursor.execute(create_eventsMetadata_query)

    event_info = []

    for event in eventsList:

        #Get Info of each Event on the page
        Event_Id = int(event['id'][9:])
        Title =  event.find('p', class_='surtitle').text.strip()
        Artists = ';'.join(list(map(str.strip, event.find('p', class_='title').find('a', class_='detail').text.split('|'))))
        Works = ';'.join(list(map(str.strip,event.find('p', class_='subtitle').text.strip().split('\n\n')[0].split('|'))))
        ImageLink = event.find('div', class_='image')['style'].split('url(')[1].split(')')[0].strip()
        Location =  event.find('p', class_='location').text.strip()
        EventDate = event['data-date']
        EventTime = ';'.join(list(map(str.strip,event.find('span', class_='time').text.split('/'))))
        
        #Create Tuple and insert in event_info list    
        event_record = (Event_Id, Title, Artists, Works, ImageLink, Location, EventDate, EventTime)
        event_info.append(event_record)

    # cursor.mogrify() to insert multiple values in EventsMetadata table
    insert_args = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s)", event).decode('utf-8')
                    for event in event_info)
    cursor.execute("INSERT INTO EventsMetadata (Event_Id, Title, Artists, Works, ImageLink, Location, EventDate, EventTime) VALUES " + (insert_args))

    conn.commit()
    rowCount = cursor.rowcount
    print(rowCount, "Record inserted successfully into EventsMetadata table")
    
except (Exception) as e:
    print("Failure occured during program execution: ",e)

finally:
    # closing database connection.
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")


