{
    'name': 'Library System',
    'version': '16.0',
    'summary': 'Faris Final Task: Library_System',
    'description': 'Library_System',
    'category': 'Productivity',
    'author': 'Rizki Faris',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'security/security_school_group_access.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/buku.xml',
        'views/Anggota.xml',
        # 'views/guru.xml',
        # 'views/pelajaran.xml',
        'views/penerbit.xml',
        'views/penulis.xml',
        'views/pinjam.xml',
        'views/kembali.xml',
    ],
    'demo': [
        'demo/Library_System_demo_data.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
