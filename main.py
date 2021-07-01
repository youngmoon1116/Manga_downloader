'''
Main file
'''

from downloader import Downloader

settings = {
    # Manga urls, should be the same website
    'manga_url': [
        'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/aabd4c95-83d4-4ddc-b2b6-bdcedf60628e/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F&_ga=2.107523970.140572903.1625176282-1885277533.1622811587',
        'URL_2'
    ],
    # Your cookies
    'cookies': 'krt.__rnd=74; _fbp=fb.1.1622811590324.1230290157; _ts_yjad=1622811591555; cookie_optin=1; _gcl_au=1.1.1906906059.1625176282; _gid=GA1.2.140572903.1625176282; cm_kp_login_account=GL; myStore=0; showSlider=0; bweternity=1aqfs7otdnhqr3di1hgdh50pjfbpvpibg9l1uqps9bkjvstq; holdBookRequestParams=%7B%22st%22%3A0%2C%22cat%22%3A0%2C%22com%22%3A0%2C%22lab%22%3A0%2C%22rf%22%3A0%2C%22r18ex%22%3A0%2C%22order%22%3A0%2C%22list%22%3A0%2C%22kw%22%3Anull%2C%22limit%22%3A50%2C%22page%22%3A1%7D; bwmember=U2FsdGVkX19oZW5seUJLV3D2DQIU1T8DW1uRgAfsPS8%3D; bwsess=9d4grf09ldfkstevcqgrq01llq; lbwsid=3010b9cacbd307fa2c85e76bb3fe8fabe6190bcd3f0f2b7ccebd49768248f3c1; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1885277533.1622811587; _ga_EPKMR4CGNW=GS1.1.1625176281.2.1.1625179895.47; _gat=1',
    # Folder names to store the Manga, the same order with manga_url
    'imgdir': [
        'IMGDIR_FOR_URL_1',
        'IMGDIR_FOR_URL_2'
    ],
    # Resolution, (Width, Height), For coma this doesn't matter.
    'res': (784, 1200),
    # Sleep time for each page (Second), normally no need to change.
    'sleep_time': 1,
    # Time wait for page loading (Second), if your network is good, you can reduce this parameter.
    'loading_wait_time': 20,
    # Cut image, (left, upper, right, lower) in pixel, None means do not cut the image. This often used to cut the edge.
    # Like (0, 0, 0, 3) means cut 3 pixel from bottom of the image.
    'cut_image': None,
    # File name prefix, if you want your file name like 'klk_v1_001.jpg', write 'klk_v1' here.
    'file_name_prefix': '',
    # File name digits count, if you want your file name like '001.jpg', write 3 here.
    'number_of_digits': 3,
    # Start page, if you want to download from 3 page, set this to 3, None means from 0
    'start_page': None,
    # End page, if you want to download until 10 page, set this to 10, None means until finished
    'end_page': None,
}

if __name__ == '__main__':
    downloader = Downloader(**settings)
    downloader.download()
