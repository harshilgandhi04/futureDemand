CREATE TABLE IF NOT EXISTS EventsMetadata(
        Event_Id  BIGINT NOT NULL  ,
        Title     VARCHAR(100) NULL,
        Artists   VARCHAR(100) NULL,
        Works     VARCHAR(100) NULL,
        ImageLink VARCHAR(500) NULL,
        Location  VARCHAR(100) NULL,
        EventDate DATE NULL        ,
        EventTime VARCHAR(50) NULL ,
        CreatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);