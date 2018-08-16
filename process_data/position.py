import random
import numpy as np
from sklearn.externals import joblib
import os

# position_classes
position_classes = ['0', '1', '2', '3', '4', '5']

# Feature List
mac_list = ['00:f6:63:0e:61:ae', 'cc:16:7e:b6:80:ce', '00:c8:8b:13:f7:fe', '00:f6:63:0e:61:a1', 'cc:16:7e:b6:80:c1', '00:c8:8b:13:f7:f1', '70:db:98:7a:f2:1e', 'cc:16:7e:b6:80:cb', 'cc:16:7e:b6:80:ca', '9a:5f:d3:3b:76:46', '00:f6:63:0e:61:a4', '00:f6:63:0e:61:a0', '00:f6:63:0e:61:a5', 'cc:16:7e:b6:80:c4', 'cc:16:7e:b6:80:c5', 'cc:16:7e:b6:80:c0', '08:17:35:c7:4f:44', '08:17:35:c7:4f:46', '08:17:35:c7:4f:4b', 'cc:16:7e:b6:80:cc', '00:f6:63:0e:61:a3', '08:17:35:c7:86:06', 'cc:16:7e:b6:80:c3', '00:c8:8b:13:f7:fc', '08:17:35:c7:4f:49', '08:17:35:c7:4f:4a', '08:17:35:c7:4f:4f', '00:c8:8b:13:f7:f4', '00:c8:8b:13:f7:f0', '70:db:98:7a:f2:11', '08:17:35:c7:86:09']

# Feature Data
position_data = [('0', {'00:f6:63:0e:61:ae': -60, 'cc:16:7e:b6:80:ce': -69, '00:c8:8b:13:f7:fe': -74, '00:f6:63:0e:61:a1': -49, 'cc:16:7e:b6:80:c1': -63, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -88, 'cc:16:7e:b6:80:cb': -69, 'cc:16:7e:b6:80:ca': -68, '9a:5f:d3:3b:76:46': -50, '00:f6:63:0e:61:a4': -43, '00:f6:63:0e:61:a0': -42, '00:f6:63:0e:61:a5': -43, 'cc:16:7e:b6:80:c4': -63, 'cc:16:7e:b6:80:c5': -65, 'cc:16:7e:b6:80:c0': -64, '08:17:35:c7:4f:44': -86, '08:17:35:c7:4f:46': -86, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -70, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -66, 'cc:16:7e:b6:80:c3': -62, '00:c8:8b:13:f7:fc': -74, '08:17:35:c7:4f:49': -86, '08:17:35:c7:4f:4a': -86, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -68, '00:c8:8b:13:f7:f0': -67, '70:db:98:7a:f2:11': -81, '08:17:35:c7:86:09': -64}),
                  ('0', {'00:f6:63:0e:61:ae': -63, 'cc:16:7e:b6:80:ce': -71, '00:c8:8b:13:f7:fe': -75, '00:f6:63:0e:61:a1': -51, 'cc:16:7e:b6:80:c1': -65, '00:c8:8b:13:f7:f1': -76, '70:db:98:7a:f2:1e': -83, 'cc:16:7e:b6:80:cb': -71, 'cc:16:7e:b6:80:ca': -72, '9a:5f:d3:3b:76:46': -51, '00:f6:63:0e:61:a4': -49, '00:f6:63:0e:61:a0': -51, '00:f6:63:0e:61:a5': -51, 'cc:16:7e:b6:80:c4': -65, 'cc:16:7e:b6:80:c5': -65, 'cc:16:7e:b6:80:c0': -64, '08:17:35:c7:4f:44': -86, '08:17:35:c7:4f:46': -84, '08:17:35:c7:4f:4b': -83, 'cc:16:7e:b6:80:cc': -71, '00:f6:63:0e:61:a3': -51, '08:17:35:c7:86:06': -81, 'cc:16:7e:b6:80:c3': -64, '00:c8:8b:13:f7:fc': -76, '08:17:35:c7:4f:49': -84, '08:17:35:c7:4f:4a': -86, '08:17:35:c7:4f:4f': -89, '00:c8:8b:13:f7:f4': -77, '00:c8:8b:13:f7:f0': -77, '70:db:98:7a:f2:11': -73, '08:17:35:c7:86:09': -73}),
                  ('0', {'00:f6:63:0e:61:ae': -54, 'cc:16:7e:b6:80:ce': -75, '00:c8:8b:13:f7:fe': -75, '00:f6:63:0e:61:a1': -54, 'cc:16:7e:b6:80:c1': -70, '00:c8:8b:13:f7:f1': -74, '70:db:98:7a:f2:1e': -83, 'cc:16:7e:b6:80:cb': -74, 'cc:16:7e:b6:80:ca': -75, '9a:5f:d3:3b:76:46': -48, '00:f6:63:0e:61:a4': -52, '00:f6:63:0e:61:a0': -53, '00:f6:63:0e:61:a5': -49, 'cc:16:7e:b6:80:c4': -68, 'cc:16:7e:b6:80:c5': -69, 'cc:16:7e:b6:80:c0': -70, '08:17:35:c7:4f:44': -79, '08:17:35:c7:4f:46': -84, '08:17:35:c7:4f:4b': -84, 'cc:16:7e:b6:80:cc': -75, '00:f6:63:0e:61:a3': -51, '08:17:35:c7:86:06': -76, 'cc:16:7e:b6:80:c3': -69, '00:c8:8b:13:f7:fc': -75, '08:17:35:c7:4f:49': -84, '08:17:35:c7:4f:4a': -89, '08:17:35:c7:4f:4f': -88, '00:c8:8b:13:f7:f4': -74, '00:c8:8b:13:f7:f0': -75, '70:db:98:7a:f2:11': -81, '08:17:35:c7:86:09': -66}),
                  ('0', {'00:f6:63:0e:61:ae': -54, 'cc:16:7e:b6:80:ce': -68, '00:c8:8b:13:f7:fe': -75, '00:f6:63:0e:61:a1': -41, 'cc:16:7e:b6:80:c1': -60, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -83, 'cc:16:7e:b6:80:cb': -68, 'cc:16:7e:b6:80:ca': -75, '9a:5f:d3:3b:76:46': -41, '00:f6:63:0e:61:a4': -41, '00:f6:63:0e:61:a0': -40, '00:f6:63:0e:61:a5': -41, 'cc:16:7e:b6:80:c4': -60, 'cc:16:7e:b6:80:c5': -60, 'cc:16:7e:b6:80:c0': -60, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -81, '08:17:35:c7:4f:4b': -81, 'cc:16:7e:b6:80:cc': -75, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -77, 'cc:16:7e:b6:80:c3': -60, '00:c8:8b:13:f7:fc': -70, '08:17:35:c7:4f:49': -81, '08:17:35:c7:4f:4a': -86, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -69, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -81, '08:17:35:c7:86:09': -75}),
                  ('0', {'00:f6:63:0e:61:ae': -54, 'cc:16:7e:b6:80:ce': -68, '00:c8:8b:13:f7:fe': -75, '00:f6:63:0e:61:a1': -47, 'cc:16:7e:b6:80:c1': -60, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -83, 'cc:16:7e:b6:80:cb': -68, 'cc:16:7e:b6:80:ca': -75, '9a:5f:d3:3b:76:46': -41, '00:f6:63:0e:61:a4': -41, '00:f6:63:0e:61:a0': -40, '00:f6:63:0e:61:a5': -41, 'cc:16:7e:b6:80:c4': -60, 'cc:16:7e:b6:80:c5': -60, 'cc:16:7e:b6:80:c0': -60, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -81, '08:17:35:c7:4f:4b': -81, 'cc:16:7e:b6:80:cc': -75, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -77, 'cc:16:7e:b6:80:c3': -60, '00:c8:8b:13:f7:fc': -70, '08:17:35:c7:4f:49': -81, '08:17:35:c7:4f:4a': -86, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -69, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -81, '08:17:35:c7:86:09': -75}),
                  ('1', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -73, '00:c8:8b:13:f7:fe': -78, '00:f6:63:0e:61:a1': -55, 'cc:16:7e:b6:80:c1': -64, '00:c8:8b:13:f7:f1': -77, '70:db:98:7a:f2:1e': -85, 'cc:16:7e:b6:80:cb': -73, 'cc:16:7e:b6:80:ca': -71, '9a:5f:d3:3b:76:46': -42, '00:f6:63:0e:61:a4': -50, '00:f6:63:0e:61:a0': -49, '00:f6:63:0e:61:a5': -50, 'cc:16:7e:b6:80:c4': -73, 'cc:16:7e:b6:80:c5': -71, 'cc:16:7e:b6:80:c0': -69, '08:17:35:c7:4f:44': -83, '08:17:35:c7:4f:46': -83, '08:17:35:c7:4f:4b': -83, 'cc:16:7e:b6:80:cc': -74, '00:f6:63:0e:61:a3': -48, '08:17:35:c7:86:06': -78, 'cc:16:7e:b6:80:c3': -71, '00:c8:8b:13:f7:fc': -78, '08:17:35:c7:4f:49': -83, '08:17:35:c7:4f:4a': -75, '08:17:35:c7:4f:4f': -89, '00:c8:8b:13:f7:f4': -74, '00:c8:8b:13:f7:f0': -70, '70:db:98:7a:f2:11': -73, '08:17:35:c7:86:09': -65}),
                  ('1', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -70, '00:c8:8b:13:f7:fe': -79, '00:f6:63:0e:61:a1': -43, 'cc:16:7e:b6:80:c1': -70, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -70, 'cc:16:7e:b6:80:ca': -70, '9a:5f:d3:3b:76:46': -47, '00:f6:63:0e:61:a4': -43, '00:f6:63:0e:61:a0': -43, '00:f6:63:0e:61:a5': -43, 'cc:16:7e:b6:80:c4': -70, 'cc:16:7e:b6:80:c5': -69, 'cc:16:7e:b6:80:c0': -70, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -81, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -70, '00:f6:63:0e:61:a3': -44, '08:17:35:c7:86:06': -77, 'cc:16:7e:b6:80:c3': -69, '00:c8:8b:13:f7:fc': -78, '08:17:35:c7:4f:49': -80, '08:17:35:c7:4f:4a': -81, '08:17:35:c7:4f:4f': -87, '00:c8:8b:13:f7:f4': -69, '00:c8:8b:13:f7:f0': -69, '70:db:98:7a:f2:11': -77, '08:17:35:c7:86:09': -66}),
                  ('1', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -70, '00:c8:8b:13:f7:fe': -79, '00:f6:63:0e:61:a1': -45, 'cc:16:7e:b6:80:c1': -70, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -70, 'cc:16:7e:b6:80:ca': -70, '9a:5f:d3:3b:76:46': -47, '00:f6:63:0e:61:a4': -43, '00:f6:63:0e:61:a0': -43, '00:f6:63:0e:61:a5': -43, 'cc:16:7e:b6:80:c4': -70, 'cc:16:7e:b6:80:c5': -69, 'cc:16:7e:b6:80:c0': -70, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -81, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -70, '00:f6:63:0e:61:a3': -44, '08:17:35:c7:86:06': -77, 'cc:16:7e:b6:80:c3': -69, '00:c8:8b:13:f7:fc': -78, '08:17:35:c7:4f:49': -80, '08:17:35:c7:4f:4a': -81, '08:17:35:c7:4f:4f': -87, '00:c8:8b:13:f7:f4': -69, '00:c8:8b:13:f7:f0': -69, '70:db:98:7a:f2:11': -77, '08:17:35:c7:86:09': -66}),
                  ('1', {'00:f6:63:0e:61:ae': -56, 'cc:16:7e:b6:80:ce': -66, '00:c8:8b:13:f7:fe': -69, '00:f6:63:0e:61:a1': -43, 'cc:16:7e:b6:80:c1': -64, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -84, 'cc:16:7e:b6:80:cb': -66, 'cc:16:7e:b6:80:ca': -65, '9a:5f:d3:3b:76:46': -46, '00:f6:63:0e:61:a4': -41, '00:f6:63:0e:61:a0': -41, '00:f6:63:0e:61:a5': -40, 'cc:16:7e:b6:80:c4': -64, 'cc:16:7e:b6:80:c5': -69, 'cc:16:7e:b6:80:c0': -64, '08:17:35:c7:4f:44': -79, '08:17:35:c7:4f:46': -79, '08:17:35:c7:4f:4b': -77, 'cc:16:7e:b6:80:cc': -66, '00:f6:63:0e:61:a3': -43, '08:17:35:c7:86:06': -79, 'cc:16:7e:b6:80:c3': -65, '00:c8:8b:13:f7:fc': -70, '08:17:35:c7:4f:49': -79, '08:17:35:c7:4f:4a': -85, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -69, '00:c8:8b:13:f7:f0': -69, '70:db:98:7a:f2:11': -78, '08:17:35:c7:86:09': -76}),
                  ('1', {'00:f6:63:0e:61:ae': -51, 'cc:16:7e:b6:80:ce': -66, '00:c8:8b:13:f7:fe': -75, '00:f6:63:0e:61:a1': -44, 'cc:16:7e:b6:80:c1': -64, '00:c8:8b:13:f7:f1': -75, '70:db:98:7a:f2:1e': -85, 'cc:16:7e:b6:80:cb': -69, 'cc:16:7e:b6:80:ca': -69, '9a:5f:d3:3b:76:46': -49, '00:f6:63:0e:61:a4': -46, '00:f6:63:0e:61:a0': -46, '00:f6:63:0e:61:a5': -46, 'cc:16:7e:b6:80:c4': -65, 'cc:16:7e:b6:80:c5': -66, 'cc:16:7e:b6:80:c0': -65, '08:17:35:c7:4f:44': -79, '08:17:35:c7:4f:46': -78, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -68, '00:f6:63:0e:61:a3': -46, '08:17:35:c7:86:06': -80, 'cc:16:7e:b6:80:c3': -65, '00:c8:8b:13:f7:fc': -75, '08:17:35:c7:4f:49': -80, '08:17:35:c7:4f:4a': -85, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -75, '00:c8:8b:13:f7:f0': -73, '70:db:98:7a:f2:11': -82, '08:17:35:c7:86:09': -86}),
                  ('2', {'00:f6:63:0e:61:ae': -55, 'cc:16:7e:b6:80:ce': -71, '00:c8:8b:13:f7:fe': -77, '00:f6:63:0e:61:a1': -44, 'cc:16:7e:b6:80:c1': -66, '00:c8:8b:13:f7:f1': -76, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -72, 'cc:16:7e:b6:80:ca': -72, '9a:5f:d3:3b:76:46': -54, '00:f6:63:0e:61:a4': -41, '00:f6:63:0e:61:a0': -41, '00:f6:63:0e:61:a5': -41, 'cc:16:7e:b6:80:c4': -65, 'cc:16:7e:b6:80:c5': -65, 'cc:16:7e:b6:80:c0': -66, '08:17:35:c7:4f:44': -84, '08:17:35:c7:4f:46': -85, '08:17:35:c7:4f:4b': -85, 'cc:16:7e:b6:80:cc': -72, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -79, 'cc:16:7e:b6:80:c3': -65, '00:c8:8b:13:f7:fc': -76, '08:17:35:c7:4f:49': -85, '08:17:35:c7:4f:4a': -85, '08:17:35:c7:4f:4f': -89, '00:c8:8b:13:f7:f4': -76, '00:c8:8b:13:f7:f0': -76, '70:db:98:7a:f2:11': -82, '08:17:35:c7:86:09': -80}),
                  ('2', {'00:f6:63:0e:61:ae': -61, 'cc:16:7e:b6:80:ce': -73, '00:c8:8b:13:f7:fe': -79, '00:f6:63:0e:61:a1': -50, 'cc:16:7e:b6:80:c1': -69, '00:c8:8b:13:f7:f1': -74, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -75, 'cc:16:7e:b6:80:ca': -74, '9a:5f:d3:3b:76:46': -57, '00:f6:63:0e:61:a4': -50, '00:f6:63:0e:61:a0': -52, '00:f6:63:0e:61:a5': -51, 'cc:16:7e:b6:80:c4': -69, 'cc:16:7e:b6:80:c5': -69, 'cc:16:7e:b6:80:c0': -69, '08:17:35:c7:4f:44': -83, '08:17:35:c7:4f:46': -84, '08:17:35:c7:4f:4b': -84, 'cc:16:7e:b6:80:cc': -73, '00:f6:63:0e:61:a3': -51, '08:17:35:c7:86:06': -77, 'cc:16:7e:b6:80:c3': -69, '00:c8:8b:13:f7:fc': -77, '08:17:35:c7:4f:49': -85, '08:17:35:c7:4f:4a': -88, '08:17:35:c7:4f:4f': -88, '00:c8:8b:13:f7:f4': -73, '00:c8:8b:13:f7:f0': -74, '70:db:98:7a:f2:11': -82, '08:17:35:c7:86:09': -80}),
                  ('2', {'00:f6:63:0e:61:ae': -61, 'cc:16:7e:b6:80:ce': -73, '00:c8:8b:13:f7:fe': -79, '00:f6:63:0e:61:a1': -52, 'cc:16:7e:b6:80:c1': -69, '00:c8:8b:13:f7:f1': -74, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -75, 'cc:16:7e:b6:80:ca': -74, '9a:5f:d3:3b:76:46': -57, '00:f6:63:0e:61:a4': -50, '00:f6:63:0e:61:a0': -52, '00:f6:63:0e:61:a5': -51, 'cc:16:7e:b6:80:c4': -69, 'cc:16:7e:b6:80:c5': -69, 'cc:16:7e:b6:80:c0': -69, '08:17:35:c7:4f:44': -83, '08:17:35:c7:4f:46': -84, '08:17:35:c7:4f:4b': -84, 'cc:16:7e:b6:80:cc': -73, '00:f6:63:0e:61:a3': -51, '08:17:35:c7:86:06': -77, 'cc:16:7e:b6:80:c3': -69, '00:c8:8b:13:f7:fc': -77, '08:17:35:c7:4f:49': -84, '08:17:35:c7:4f:4a': -88, '08:17:35:c7:4f:4f': -88, '00:c8:8b:13:f7:f4': -73, '00:c8:8b:13:f7:f0': -74, '70:db:98:7a:f2:11': -82, '08:17:35:c7:86:09': -80}),
                  ('2', {'00:f6:63:0e:61:ae': -61, 'cc:16:7e:b6:80:ce': -71, '00:c8:8b:13:f7:fe': -77, '00:f6:63:0e:61:a1': -51, 'cc:16:7e:b6:80:c1': -74, '00:c8:8b:13:f7:f1': -74, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -71, 'cc:16:7e:b6:80:ca': -71, '9a:5f:d3:3b:76:46': -50, '00:f6:63:0e:61:a4': -52, '00:f6:63:0e:61:a0': -53, '00:f6:63:0e:61:a5': -50, 'cc:16:7e:b6:80:c4': -70, 'cc:16:7e:b6:80:c5': -70, 'cc:16:7e:b6:80:c0': -76, '08:17:35:c7:4f:44': -82, '08:17:35:c7:4f:46': -82, '08:17:35:c7:4f:4b': -84, 'cc:16:7e:b6:80:cc': -71, '00:f6:63:0e:61:a3': -53, '08:17:35:c7:86:06': -78, 'cc:16:7e:b6:80:c3': -69, '00:c8:8b:13:f7:fc': -78, '08:17:35:c7:4f:49': -82, '08:17:35:c7:4f:4a': -85, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -73, '00:c8:8b:13:f7:f0': -74, '70:db:98:7a:f2:11': -78, '08:17:35:c7:86:09': -80}),
                  ('2', {'00:f6:63:0e:61:ae': -54, 'cc:16:7e:b6:80:ce': -71, '00:c8:8b:13:f7:fe': -79, '00:f6:63:0e:61:a1': -50, 'cc:16:7e:b6:80:c1': -69, '00:c8:8b:13:f7:f1': -72, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -68, 'cc:16:7e:b6:80:ca': -73, '9a:5f:d3:3b:76:46': -45, '00:f6:63:0e:61:a4': -54, '00:f6:63:0e:61:a0': -54, '00:f6:63:0e:61:a5': -55, 'cc:16:7e:b6:80:c4': -67, 'cc:16:7e:b6:80:c5': -69, 'cc:16:7e:b6:80:c0': -70, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -82, '08:17:35:c7:4f:4b': -83, 'cc:16:7e:b6:80:cc': -72, '00:f6:63:0e:61:a3': -54, '08:17:35:c7:86:06': -81, 'cc:16:7e:b6:80:c3': -69, '00:c8:8b:13:f7:fc': -80, '08:17:35:c7:4f:49': -82, '08:17:35:c7:4f:4a': -85, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -73, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -78, '08:17:35:c7:86:09': -81}),
                  ('3', {'00:f6:63:0e:61:ae': -58, 'cc:16:7e:b6:80:ce': -72, '00:c8:8b:13:f7:fe': -73, '00:f6:63:0e:61:a1': -48, 'cc:16:7e:b6:80:c1': -71, '00:c8:8b:13:f7:f1': -74, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -71, 'cc:16:7e:b6:80:ca': -71, '9a:5f:d3:3b:76:46': -47, '00:f6:63:0e:61:a4': -41, '00:f6:63:0e:61:a0': -41, '00:f6:63:0e:61:a5': -41, 'cc:16:7e:b6:80:c4': -70, 'cc:16:7e:b6:80:c5': -71, 'cc:16:7e:b6:80:c0': -71, '08:17:35:c7:4f:44': -78, '08:17:35:c7:4f:46': -78, '08:17:35:c7:4f:4b': -77, 'cc:16:7e:b6:80:cc': -71, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -75, 'cc:16:7e:b6:80:c3': -72, '00:c8:8b:13:f7:fc': -74, '08:17:35:c7:4f:49': -78, '08:17:35:c7:4f:4a': -84, '08:17:35:c7:4f:4f': -84, '00:c8:8b:13:f7:f4': -73, '00:c8:8b:13:f7:f0': -71, '70:db:98:7a:f2:11': -78, '08:17:35:c7:86:09': -78}),
                  ('3', {'00:f6:63:0e:61:ae': -58, 'cc:16:7e:b6:80:ce': -66, '00:c8:8b:13:f7:fe': -75, '00:f6:63:0e:61:a1': -52, 'cc:16:7e:b6:80:c1': -67, '00:c8:8b:13:f7:f1': -62, '70:db:98:7a:f2:1e': -81, 'cc:16:7e:b6:80:cb': -67, 'cc:16:7e:b6:80:ca': -66, '9a:5f:d3:3b:76:46': -51, '00:f6:63:0e:61:a4': -53, '00:f6:63:0e:61:a0': -53, '00:f6:63:0e:61:a5': -53, 'cc:16:7e:b6:80:c4': -67, 'cc:16:7e:b6:80:c5': -67, 'cc:16:7e:b6:80:c0': -66, '08:17:35:c7:4f:44': -83, '08:17:35:c7:4f:46': -81, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -66, '00:f6:63:0e:61:a3': -53, '08:17:35:c7:86:06': -64, 'cc:16:7e:b6:80:c3': -67, '00:c8:8b:13:f7:fc': -74, '08:17:35:c7:4f:49': -80, '08:17:35:c7:4f:4a': -89, '08:17:35:c7:4f:4f': -89, '00:c8:8b:13:f7:f4': -62, '00:c8:8b:13:f7:f0': -59, '70:db:98:7a:f2:11': -70, '08:17:35:c7:86:09': -67}),
                  ('3', {'00:f6:63:0e:61:ae': -58, 'cc:16:7e:b6:80:ce': -67, '00:c8:8b:13:f7:fe': -71, '00:f6:63:0e:61:a1': -51, 'cc:16:7e:b6:80:c1': -64, '00:c8:8b:13:f7:f1': -65, '70:db:98:7a:f2:1e': -75, 'cc:16:7e:b6:80:cb': -67, 'cc:16:7e:b6:80:ca': -66, '9a:5f:d3:3b:76:46': -51, '00:f6:63:0e:61:a4': -50, '00:f6:63:0e:61:a0': -50, '00:f6:63:0e:61:a5': -49, 'cc:16:7e:b6:80:c4': -64, 'cc:16:7e:b6:80:c5': -64, 'cc:16:7e:b6:80:c0': -63, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -80, '08:17:35:c7:4f:4b': -80, 'cc:16:7e:b6:80:cc': -66, '00:f6:63:0e:61:a3': -50, '08:17:35:c7:86:06': -74, 'cc:16:7e:b6:80:c3': -64, '00:c8:8b:13:f7:fc': -72, '08:17:35:c7:4f:49': -80, '08:17:35:c7:4f:4a': -86, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -65, '00:c8:8b:13:f7:f0': -63, '70:db:98:7a:f2:11': -73, '08:17:35:c7:86:09': -74}),
                 ('3', {'00:f6:63:0e:61:ae': -58, 'cc:16:7e:b6:80:ce': -68, '00:c8:8b:13:f7:fe': -70, '00:f6:63:0e:61:a1': -53, 'cc:16:7e:b6:80:c1': -63, '00:c8:8b:13:f7:f1': -66, '70:db:98:7a:f2:1e': -73, 'cc:16:7e:b6:80:cb': -67, 'cc:16:7e:b6:80:ca': -66, '9a:5f:d3:3b:76:46': -52, '00:f6:63:0e:61:a4': -49, '00:f6:63:0e:61:a0': -49, '00:f6:63:0e:61:a5': -48, 'cc:16:7e:b6:80:c4': -63, 'cc:16:7e:b6:80:c5': -63, 'cc:16:7e:b6:80:c0': -63, '08:17:35:c7:4f:44': -80, '08:17:35:c7:4f:46': -80, '08:17:35:c7:4f:4b': -80, 'cc:16:7e:b6:80:cc': -67, '00:f6:63:0e:61:a3': -50, '08:17:35:c7:86:06': -77, 'cc:16:7e:b6:80:c3': -63, '00:c8:8b:13:f7:fc': -72, '08:17:35:c7:4f:49': -80, '08:17:35:c7:4f:4a': -85, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -66, '00:c8:8b:13:f7:f0': -65, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -76}),
                 ('3', {'00:f6:63:0e:61:ae': -58, 'cc:16:7e:b6:80:ce': -73, '00:c8:8b:13:f7:fe': -72, '00:f6:63:0e:61:a1': -50, 'cc:16:7e:b6:80:c1': -64, '00:c8:8b:13:f7:f1': -70, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -73, 'cc:16:7e:b6:80:ca': -71, '9a:5f:d3:3b:76:46': -48, '00:f6:63:0e:61:a4': -47, '00:f6:63:0e:61:a0': -46, '00:f6:63:0e:61:a5': -48, 'cc:16:7e:b6:80:c4': -65, 'cc:16:7e:b6:80:c5': -65, 'cc:16:7e:b6:80:c0': -65, '08:17:35:c7:4f:44': -84, '08:17:35:c7:4f:46': -81, '08:17:35:c7:4f:4b': -83, 'cc:16:7e:b6:80:cc': -68, '00:f6:63:0e:61:a3': -48, '08:17:35:c7:86:06': -71, 'cc:16:7e:b6:80:c3': -64, '00:c8:8b:13:f7:fc': -73, '08:17:35:c7:4f:49': -83, '08:17:35:c7:4f:4a': -84, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -66, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -67, '08:17:35:c7:86:09': -69}), ('3', {'00:f6:63:0e:61:ae': -58, 'cc:16:7e:b6:80:ce': -73, '00:c8:8b:13:f7:fe': -72, '00:f6:63:0e:61:a1': -52, 'cc:16:7e:b6:80:c1': -64, '00:c8:8b:13:f7:f1': -70, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -73, 'cc:16:7e:b6:80:ca': -71, '9a:5f:d3:3b:76:46': -48, '00:f6:63:0e:61:a4': -47, '00:f6:63:0e:61:a0': -46, '00:f6:63:0e:61:a5': -48, 'cc:16:7e:b6:80:c4': -65, 'cc:16:7e:b6:80:c5': -65, 'cc:16:7e:b6:80:c0': -65, '08:17:35:c7:4f:44': -84, '08:17:35:c7:4f:46': -81, '08:17:35:c7:4f:4b': -83, 'cc:16:7e:b6:80:cc': -68, '00:f6:63:0e:61:a3': -48, '08:17:35:c7:86:06': -71, 'cc:16:7e:b6:80:c3': -64, '00:c8:8b:13:f7:fc': -73, '08:17:35:c7:4f:49': -83, '08:17:35:c7:4f:4a': -84, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -66, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -67, '08:17:35:c7:86:09': -69}), ('4', {'00:f6:63:0e:61:ae': -57, 'cc:16:7e:b6:80:ce': -70, '00:c8:8b:13:f7:fe': -75, '00:f6:63:0e:61:a1': -45, 'cc:16:7e:b6:80:c1': -67, '00:c8:8b:13:f7:f1': -71, '70:db:98:7a:f2:1e': -85, 'cc:16:7e:b6:80:cb': -70, 'cc:16:7e:b6:80:ca': -70, '9a:5f:d3:3b:76:46': -48, '00:f6:63:0e:61:a4': -47, '00:f6:63:0e:61:a0': -46, '00:f6:63:0e:61:a5': -50, 'cc:16:7e:b6:80:c4': -68, 'cc:16:7e:b6:80:c5': -66, 'cc:16:7e:b6:80:c0': -67, '08:17:35:c7:4f:44': -86, '08:17:35:c7:4f:46': -82, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -71, '00:f6:63:0e:61:a3': -49, '08:17:35:c7:86:06': -81, 'cc:16:7e:b6:80:c3': -67, '00:c8:8b:13:f7:fc': -76, '08:17:35:c7:4f:49': -87, '08:17:35:c7:4f:4a': -88, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -61, '00:c8:8b:13:f7:f0': -71, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -76}), ('4', {'00:f6:63:0e:61:ae': -57, 'cc:16:7e:b6:80:ce': -70, '00:c8:8b:13:f7:fe': -75, '00:f6:63:0e:61:a1': -45, 'cc:16:7e:b6:80:c1': -67, '00:c8:8b:13:f7:f1': -71, '70:db:98:7a:f2:1e': -85, 'cc:16:7e:b6:80:cb': -70, 'cc:16:7e:b6:80:ca': -70, '9a:5f:d3:3b:76:46': -48, '00:f6:63:0e:61:a4': -47, '00:f6:63:0e:61:a0': -46, '00:f6:63:0e:61:a5': -50, 'cc:16:7e:b6:80:c4': -68, 'cc:16:7e:b6:80:c5': -66, 'cc:16:7e:b6:80:c0': -67, '08:17:35:c7:4f:44': -86, '08:17:35:c7:4f:46': -82, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -71, '00:f6:63:0e:61:a3': -49, '08:17:35:c7:86:06': -81, 'cc:16:7e:b6:80:c3': -67, '00:c8:8b:13:f7:fc': -76, '08:17:35:c7:4f:49': -87, '08:17:35:c7:4f:4a': -88, '08:17:35:c7:4f:4f': -86, '00:c8:8b:13:f7:f4': -61, '00:c8:8b:13:f7:f0': -71, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -76}), ('4', {'00:f6:63:0e:61:ae': -57, 'cc:16:7e:b6:80:ce': -71, '00:c8:8b:13:f7:fe': -73, '00:f6:63:0e:61:a1': -46, 'cc:16:7e:b6:80:c1': -63, '00:c8:8b:13:f7:f1': -70, '70:db:98:7a:f2:1e': -85, 'cc:16:7e:b6:80:cb': -72, 'cc:16:7e:b6:80:ca': -72, '9a:5f:d3:3b:76:46': -47, '00:f6:63:0e:61:a4': -46, '00:f6:63:0e:61:a0': -45, '00:f6:63:0e:61:a5': -46, 'cc:16:7e:b6:80:c4': -63, 'cc:16:7e:b6:80:c5': -63, 'cc:16:7e:b6:80:c0': -65, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -82, '08:17:35:c7:4f:4b': -81, 'cc:16:7e:b6:80:cc': -72, '00:f6:63:0e:61:a3': -45, '08:17:35:c7:86:06': -69, 'cc:16:7e:b6:80:c3': -63, '00:c8:8b:13:f7:fc': -74, '08:17:35:c7:4f:49': -81, '08:17:35:c7:4f:4a': -87, '08:17:35:c7:4f:4f': -87, '00:c8:8b:13:f7:f4': -70, '00:c8:8b:13:f7:f0': -71, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -78}), ('4', {'00:f6:63:0e:61:ae': -57, 'cc:16:7e:b6:80:ce': -67, '00:c8:8b:13:f7:fe': -73, '00:f6:63:0e:61:a1': -38, 'cc:16:7e:b6:80:c1': -66, '00:c8:8b:13:f7:f1': -67, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -67, 'cc:16:7e:b6:80:ca': -67, '9a:5f:d3:3b:76:46': -49, '00:f6:63:0e:61:a4': -38, '00:f6:63:0e:61:a0': -38, '00:f6:63:0e:61:a5': -38, 'cc:16:7e:b6:80:c4': -66, 'cc:16:7e:b6:80:c5': -65, 'cc:16:7e:b6:80:c0': -64, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -74, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -68, '00:f6:63:0e:61:a3': -38, '08:17:35:c7:86:06': -77, 'cc:16:7e:b6:80:c3': -66, '00:c8:8b:13:f7:fc': -74, '08:17:35:c7:4f:49': -73, '08:17:35:c7:4f:4a': -87, '08:17:35:c7:4f:4f': -87, '00:c8:8b:13:f7:f4': -67, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -64}), ('5', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -69, '00:c8:8b:13:f7:fe': -73, '00:f6:63:0e:61:a1': -46, 'cc:16:7e:b6:80:c1': -61, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -68, 'cc:16:7e:b6:80:ca': -69, '9a:5f:d3:3b:76:46': -56, '00:f6:63:0e:61:a4': -48, '00:f6:63:0e:61:a0': -47, '00:f6:63:0e:61:a5': -48, 'cc:16:7e:b6:80:c4': -61, 'cc:16:7e:b6:80:c5': -60, 'cc:16:7e:b6:80:c0': -61, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -80, '08:17:35:c7:4f:4b': -81, 'cc:16:7e:b6:80:cc': -70, '00:f6:63:0e:61:a3': -49, '08:17:35:c7:86:06': -79, 'cc:16:7e:b6:80:c3': -61, '00:c8:8b:13:f7:fc': -74, '08:17:35:c7:4f:49': -82, '08:17:35:c7:4f:4a': -87, '08:17:35:c7:4f:4f': -87, '00:c8:8b:13:f7:f4': -68, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -73}), ('5', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -75, '00:c8:8b:13:f7:fe': -82, '00:f6:63:0e:61:a1': -38, 'cc:16:7e:b6:80:c1': -61, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -73, 'cc:16:7e:b6:80:ca': -73, '9a:5f:d3:3b:76:46': -49, '00:f6:63:0e:61:a4': -40, '00:f6:63:0e:61:a0': -39, '00:f6:63:0e:61:a5': -40, 'cc:16:7e:b6:80:c4': -74, 'cc:16:7e:b6:80:c5': -74, 'cc:16:7e:b6:80:c0': -72, '08:17:35:c7:4f:44': -82, '08:17:35:c7:4f:46': -82, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -74, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -75, 'cc:16:7e:b6:80:c3': -61, '00:c8:8b:13:f7:fc': -83, '08:17:35:c7:4f:49': -83, '08:17:35:c7:4f:4a': -85, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -68, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -75}), ('5', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -75, '00:c8:8b:13:f7:fe': -82, '00:f6:63:0e:61:a1': -43, 'cc:16:7e:b6:80:c1': -61, '00:c8:8b:13:f7:f1': -69, '70:db:98:7a:f2:1e': -86, 'cc:16:7e:b6:80:cb': -73, 'cc:16:7e:b6:80:ca': -73, '9a:5f:d3:3b:76:46': -49, '00:f6:63:0e:61:a4': -40, '00:f6:63:0e:61:a0': -39, '00:f6:63:0e:61:a5': -40, 'cc:16:7e:b6:80:c4': -74, 'cc:16:7e:b6:80:c5': -74, 'cc:16:7e:b6:80:c0': -72, '08:17:35:c7:4f:44': -82, '08:17:35:c7:4f:46': -82, '08:17:35:c7:4f:4b': -82, 'cc:16:7e:b6:80:cc': -74, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -75, 'cc:16:7e:b6:80:c3': -61, '00:c8:8b:13:f7:fc': -83, '08:17:35:c7:4f:49': -83, '08:17:35:c7:4f:4a': -85, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -68, '00:c8:8b:13:f7:f0': -68, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -75}), ('5', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -72, '00:c8:8b:13:f7:fe': -82, '00:f6:63:0e:61:a1': -46, 'cc:16:7e:b6:80:c1': -65, '00:c8:8b:13:f7:f1': -66, '70:db:98:7a:f2:1e': -89, 'cc:16:7e:b6:80:cb': -72, 'cc:16:7e:b6:80:ca': -72, '9a:5f:d3:3b:76:46': -52, '00:f6:63:0e:61:a4': -41, '00:f6:63:0e:61:a0': -41, '00:f6:63:0e:61:a5': -41, 'cc:16:7e:b6:80:c4': -66, 'cc:16:7e:b6:80:c5': -67, 'cc:16:7e:b6:80:c0': -65, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -80, '08:17:35:c7:4f:4b': -81, 'cc:16:7e:b6:80:cc': -72, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -73, 'cc:16:7e:b6:80:c3': -65, '00:c8:8b:13:f7:fc': -81, '08:17:35:c7:4f:49': -83, '08:17:35:c7:4f:4a': -81, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -66, '00:c8:8b:13:f7:f0': -66, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -79}), ('5', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -72, '00:c8:8b:13:f7:fe': -82, '00:f6:63:0e:61:a1': -41, 'cc:16:7e:b6:80:c1': -65, '00:c8:8b:13:f7:f1': -66, '70:db:98:7a:f2:1e': -89, 'cc:16:7e:b6:80:cb': -72, 'cc:16:7e:b6:80:ca': -72, '9a:5f:d3:3b:76:46': -52, '00:f6:63:0e:61:a4': -41, '00:f6:63:0e:61:a0': -41, '00:f6:63:0e:61:a5': -41, 'cc:16:7e:b6:80:c4': -66, 'cc:16:7e:b6:80:c5': -67, 'cc:16:7e:b6:80:c0': -65, '08:17:35:c7:4f:44': -81, '08:17:35:c7:4f:46': -80, '08:17:35:c7:4f:4b': -81, 'cc:16:7e:b6:80:cc': -72, '00:f6:63:0e:61:a3': -41, '08:17:35:c7:86:06': -73, 'cc:16:7e:b6:80:c3': -65, '00:c8:8b:13:f7:fc': -81, '08:17:35:c7:4f:49': -83, '08:17:35:c7:4f:4a': -81, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -66, '00:c8:8b:13:f7:f0': -66, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -79}), ('5', {'00:f6:63:0e:61:ae': -53, 'cc:16:7e:b6:80:ce': -70, '00:c8:8b:13:f7:fe': -77, '00:f6:63:0e:61:a1': -39, 'cc:16:7e:b6:80:c1': -64, '00:c8:8b:13:f7:f1': -64, '70:db:98:7a:f2:1e': -87, 'cc:16:7e:b6:80:cb': -70, 'cc:16:7e:b6:80:ca': -70, '9a:5f:d3:3b:76:46': -55, '00:f6:63:0e:61:a4': -36, '00:f6:63:0e:61:a0': -35, '00:f6:63:0e:61:a5': -35, 'cc:16:7e:b6:80:c4': -66, 'cc:16:7e:b6:80:c5': -67, 'cc:16:7e:b6:80:c0': -65, '08:17:35:c7:4f:44': -78, '08:17:35:c7:4f:46': -80, '08:17:35:c7:4f:4b': -80, 'cc:16:7e:b6:80:cc': -70, '00:f6:63:0e:61:a3': -37, '08:17:35:c7:86:06': -73, 'cc:16:7e:b6:80:c3': -61, '00:c8:8b:13:f7:fc': -77, '08:17:35:c7:4f:49': -81, '08:17:35:c7:4f:4a': -81, '08:17:35:c7:4f:4f': -85, '00:c8:8b:13:f7:f4': -66, '00:c8:8b:13:f7:f0': -65, '70:db:98:7a:f2:11': -75, '08:17:35:c7:86:09': -72})]


# allocate the test space and train space
# deprecated in last version
def test_train_allo(position_dict):
    position_list = {}
    variance_list = []
    for dict_p in position_dict:
        if dict_p[0] not in position_list:
            position_list[dict_p[0]] = []
            variance_list.append(list(dict_p[1].values()))
        else:
            position_list[dict_p[0]].append([dict_p[1]])
            variance_list.append(list(dict_p[1].values()))


    train_data = []
    test_data = []
    ratio = 0.7
    variance_list = np.array(variance_list)
    unitlize = [np.min(variance_list), np.max(variance_list), np.min(variance_list)]
    std = np.std(variance_list, axis=0)
    std_flag = 2.5
    index = np.argwhere(std > std_flag)
    index = index.reshape(len(index))

    for label, value in position_list.items():
        n = len(value)
        random.shuffle(value)
        train_l = value[0:int(ratio * n)]
        set_l = value[int(ratio * n):]
        for sets in train_l:
            sets = np.array(list(sets[0].values()))
            sets = sets[index]
            train_data.append((label, list(sets)))
        for sets in set_l:
            sets = np.array(list(sets[0].values()))
            sets = sets[index]
            test_data.append((label, list(sets)))

    # variance_list = variance_list[:, index]
    return train_data, test_data, len(index), unitlize

# generate numpy data from original txt file for model
def GenerateData():
    filepath = os.path.abspath(os.path.join(os.getcwd()))+"/data/"
    p_d = joblib.load(filepath + "TrainSet.dat")
    position_data = p_d['data']
    position_label = p_d['target']
    mac_list = p_d['feature_names']
    position_data = (position_data - np.min(position_data)) / (np.max(position_data) - np.min(position_data))

    # path = os.path.abspath('..')
    # fr = open("position_data.txt")
    # position_da = fr.read()
    # dict_name = eval(position_da)
    # train_set, test_set, index, unitlize = test_train_allo(dict_name)
    # fr.close()
    # mac_list = mac_list[0:index]

    # #-----------------numpy array version---------------
    # trainData, trainLabel = [], []
    # for trainSet in train_set:
    #     trainData.append(trainSet[1])
    #     trainLabel.append(trainSet[0])
    # trainData = np.array(trainData)
    # trainLabel = np.array(trainLabel)
    #
    # testData, testLabel = [], []
    # for testSet in test_set:
    #     testData.append(testSet[1])
    #     testLabel.append(testSet[0])
    # testData = np.array(testData)
    # testLabel = np.array(testLabel)
    # trainData = (trainData - unitlize[0]) / (unitlize[1] - unitlize[2])
    # testData = (testData - unitlize[0]) / (unitlize[1] - unitlize[2])
    # --------------------------------------------------------

    # -----------------list array version----------------
    # trainData, trainLabel = [], []
    # for trainSet in train_set:
    #     trainData.append(trainSet[0])
    #     trainLabel.append(trainSet[1])
    #
    # testData, testLabel = [], []
    # for testSet in test_set:
    #     testData.append(testSet[0])
    #     testLabel.append(testSet[1])
    # -----------------------------------------------------

    return position_classes, position_data, position_label
    # return position_classes, trainData, trainLabel, testData, testLabel


if __name__ == "__main__":
    a, b, c, d = GenerateData()
    print(a)
    print(b)
    for i in c:
        print(i)
    for j in d:
        print(j)
