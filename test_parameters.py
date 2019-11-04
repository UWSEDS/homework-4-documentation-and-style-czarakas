"""
Sets parameters about which dataframe to test
"""

import ReadInData
THIS_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
DF = ReadInData.create_dataframe(THIS_URL)
COLUMN_NAMES = ['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']
COLUMN_TYPES = [str, float, float]
