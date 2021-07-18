import xml.etree.ElementTree as etree

file = 'Death_By_Zero_S1E7_A17235-007_Metadata.xml.txt'
parser = etree.XMLParser(encoding="UTF-8")
tree = etree.parse(file, parser)
root = tree.getroot()

data_metadata = root.find("Metadata")
for app_data in data_metadata.findall("AMS"):
    if app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Package_Asset":
        app_data.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Package_Asset"
        app_data.attrib["Asset_ID"] = "FAIR0100000172350151"
        app_data.attrib["Description"] = "Death_By_Zero_S1E15_Package_Asset"

data_asset = root.find("Asset")

asset_metadata = data_asset.find("Metadata")
for app_data in asset_metadata.find("AMS"):
    if app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Title_Asset":
        app_data.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Title_Asset"
        app_data.attrib["Asset_ID"] = "FAIR0100000172350152"
        app_data.attrib["Description"] = "Death_By_Zero_S1E15_Title_Asset"
for app_data in asset_metadata.findall("App_Data"):
    if app_data.attrib["Name"] == "Title":
        app_data.attrib["Value"] = "Death By Zero S1E15"
    if app_data.attrib["Name"] == "Title_Brief":
        app_data.attrib["Value"] = "DeathByZero S1E15"
    if app_data.attrib["Name"] == "Episode_Name":
        app_data.attrib["Value"] = "Death By Zero S1E15"
    if app_data.attrib["Name"] == "Episode_ID":
        app_data.attrib["Value"] = "S01E15"
    if app_data.attrib["Name"] == "Licensing_Window_Start":
        app_data.attrib["Value"] = "2021-08-18"

for app_data in data_asset.findall("Asset"):
    asset_metadata_2 = app_data.find("Metadata")
    app_data_2 = asset_metadata_2.find("AMS")
    if app_data_2.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Movie_Asset":
        app_data_2.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Movie_Asset"
        app_data_2.attrib["Asset_ID"] = "FAIR0100000172350153"
        app_data_2.attrib["Description"] = "Death_By_Zero_S1E15_Movie_Asset"
    elif app_data_2.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Poster_Asset":
        app_data_2.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Poster_Asset"
        app_data_2.attrib["Asset_ID"] = "FAIR0100000172350154"
        app_data_2.attrib["Description"] = "Death_By_Zero_S1E15_Poster_Asset"

    asset_metadata_3 = app_data.find("Content")
    if asset_metadata_3.attrib["Value"] == "Death_By_Zero_S1E7_A17235-007_HD_Drama.mxf":
        asset_metadata_3.attrib["Value"] = "Death_By_Zero_S1E15_A17235-015_HD_Drama.mxf"
    if asset_metadata_3.attrib["Value"] == "Death_By_Zero_S1E7_A17235-007_Poster.jpg":
        asset_metadata_3.attrib["Value"] = "Death_By_Zero_S1E15_A17235-015_Poster.jpg"





# data_asset_2 = data_asset.findall("Asset")
# asset_metadata_2 = data_asset_2.findall("Metadata")
# for app_data in asset_metadata_2.findall("AMS"):
#     if app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Movie_Asset":
#             app_data.attrib["Asset_ID"] = "Testing................"
#     elif app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Poster_Asset":
#             app_data.attrib["Asset_ID"] = "TEST...TEST..TEST"

# data_asset_2 = data_asset.find("Asset")
# asset_metadata_2 = data_asset_2.find("Metadata")
# for app_data in asset_metadata_2.findall("AMS"):
#       if app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Poster_Asset":
#         app_data.attrib["Asset_ID"] = "TEST...TEST..TEST"
# asset_metadata_movie = data_asset_movie.find("Metadata")
# asset_metadata_movie_ams = asset_metadata_movie.find("AMS")
# if asset_metadata_movie_ams.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Movie_Asset":
#     asset_metadata_movie_ams.attrib["Asset_Name"] = "........TESTING........."
# asset_metadata_movie_content = data_asset_movie.find("Content")
# asset_metadata_movie_content.attrib["Value"] = "Death_By_Zero_S1E15_A17235-015_HD_Drama.mxf"
#
# data_asset_poster = data_asset.find("Asset")
# asset_metadata_poster = data_asset_poster.find("Metadata")
# asset_metadata_poster_ams = asset_metadata_poster.find("AMS")
# if asset_metadata_poster_ams.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Poster_Asset":
#     asset_metadata_poster_ams.attrib["Asset_Name"] = "TESTING..testing......."
# asset_metadata_poster_content = data_asset_poster.find("Content")
# asset_metadata_poster_content.attrib["Value"] = "Death_By_Zero_S1E15_A17235-015_Poster.jpg"

tree.write("Death_By_Zero_S1E15_A17235-015_Metadata.xml")

# Section 1
# package_asset = myroot.find("Metadata")
# for app_data in package_asset.findall("AMS"):
#     if app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Package_Asset":
#         app_data.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Package_Asset"
#         app_data.attrib["Asset_ID"] = "FAIR0100000172350151"
#         app_data.attrib["Description"] = "Death_By_Zero_S1E15_Package_Asset"
#     elif app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Title_Asset":
#         app_data.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Title_Asset"
#         app_data.attrib["Asset_ID"] = "FAIR0100000172350152"
#         app_data.attrib["Description"] = "Death_By_Zero_S1E15_Title_Asset"


# Section 2
# two_asset = myroot.find("Asset")
# asset_metadata = two_asset.find("Metadata")
# for app_data in asset_metadata.findall("AMS"):
#     if


# for app_data in asset_metadata.findall("App_Data"):
#         if app_data.attrib["Name"] == "Title":
#             app_data.attrib["Value"] = "Death By Zero S1E15"
#         elif app_data.attrib["Name"] == "Title_Brief":
#             app_data.attrib["Value"] = "DeathByZero S1E15"
#         elif app_data.attrib["Name"] == "Episode_Name":
#             app_data.attrib["Value"] = "Death By Zero S1E15"
#         elif app_data.attrib["Name"] == "Episode_ID":
#             app_data.attrib["Value"] = "S01E12"
#         elif app_data.attrib["Name"] == "Licensing_Window_Start":
#             app_data.attrib["Value"] = "2021-08-07"

# Section 3
# three_asset = two_asset.find("Asset")
# three_metadata = three_asset.find("Metadata")
# for app_data in three_metadata.findall("AMS"):
#     if app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Movie_Asset":
#         app_data.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Movie_Asset"
#         app_data.attrib["Asset_ID"] = "FAIR0100000172350153"
#         app_data.attrib["Description"] = "Death_By_Zero_S1E15_Movie_Asset"
#     elif app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Poster_Asset":
#         app_data.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Poster_Asset"
#         app_data.attrib["Asset_ID"] = "FAIR0100000172350154"
#         app_data.attrib["Description"] = "Death_By_Zero_S1E15_Poster_Asset"
#
# for app_data in three_asset.findall("Content"):
#     app_data.attrib["Value"] = "Death_By_Zero_S1E15_A17235-015_HD_Drama.mxf"


# Section 4
# four_asset = three_asset.find("Asset")
# # four_metadata = four_asset.find("Metadata")
# for app_data in three_metadata.findall("AMS"):
#     if app_data.attrib["Asset_Name"] == "Death_By_Zero_S1E7_A17235-007_Poster_Asset":
#         app_data.attrib["Asset_Name"] = "Death_By_Zero_S1E15_A17235-015_Poster_Asset"
#         app_data.attrib["Asset_ID"] = "FAIR0100000172350154"
#         app_data.attrib["Description"] = "Death_By_Zero_S1E15_Poster_Asset"
# for app_data in three_asset.findall("Content"):
#     app_data.attrib["Value"] = "Death_By_Zero_S1E15_A17235-015_Poster.jpg"
