# from elastic_feeder.scripts.commands import command

# command()


from elastic_feeder.controller import FeedElastic
fd = FeedElastic(
        host="10.2.140.1", 
        port=9200,
        filename="/Users/hasanaliyev/Documents/programming/gitlab/onneks/btx/es_map/baku_map/Unvanlar-translate.csv",
        index="unvanlar",
        
        properties={
            "street_az": {
                "type": "search_as_you_type",
            },
             "street_ru": {
                "type": "search_as_you_type",

            },
             "street_en": {
                "type": "search_as_you_type",

            },
             "house_number": {
                "type": "search_as_you_type",

            },
             "city": {
                "type": "search_as_you_type",

            },
            "coord": {
                "type": "geo_point"
            }
        }
    )

print(fd.run())