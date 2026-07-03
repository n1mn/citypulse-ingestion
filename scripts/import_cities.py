from app.etl.city_import_pipeline import import_cities

def main():
    import_cities("data/worldcities.csv")

if __name__ == "__main__":
    main()