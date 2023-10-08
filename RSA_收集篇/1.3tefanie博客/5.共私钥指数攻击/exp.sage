
#sage
import gmpy2
import libnum

e0=int('0x1589b1732d8ce5aedf1e34a63a14bac68dcc11ee18b94e293efe58c2b77d055db463503a039472eff881b504b90e6bec1c90da3efb02c6b94770ada0a921eb5e9d19a4ca1d26b47cbaee855b72da5a79a9acb675e48c46140063e53ce1a9b74c826a1173f720ad01681bb06ad6e993d953c25f854b01107f90b7ed1db62df4f1',16)
n0=int('0x4c9a771c771a499f13436e8b1e237db8bd03085297501421b08c4aad841fe078bbe3a916f24555b64b322a81d59c6bbecc9d61821406d61d59932ddebef621180f4df2b7cb4198de92609fec4cfabf4ae25abf3a1817550d1a32ce91c65974c21dea804a536d1b659458344535ed756dd9bbc683642405d1f09dbc17815ec031',16)
c0=int('0x40b12da27be9bd9f40b2462fba93786d1a0cf22aa1adc22597854f5be0856fe53031ec6cfb30f43397c6d42f4b935914a6ea448a531517f05200abd13d5777e718cc88c16bdd432a2536c1e7f6c31e78f223a3b17935c565030b497ffe2a91177b32634bb0affcb81ddce96c031548eb312faf3038386154202a9d7dcfd75061',16)


e1=int('0x382abe54e39f9f447fa8d0e5a7d7c9487dc25e3d82045dcadc119e4bb357436cf1f87a000e8b28ec0427cc64578dc7e17bf81935cf9d6ce9f0da262c192e63fe83ec83b50083f5f9843fcad6bd86da5e69cfbaaa4583e473ae3ac3acdc472b194cf0f37c085b6599418d12ed97d54f339a75f353958c9836097a6379ceb742fd',16)
n1=int('0xf092a041b286be8d44ec5ecfaf0504e5ed9353fa56746c6a4dab91dc684bcedf5260970c8b9f66bc470fbb4bc3d326108c2cf0502e01e38aa18faa0c626658272d507e9ececb66c927efbd6aa51c2ce6f3c47207faf94b7e385a29e85fe6d79d27eed0f4bd87a22f2a849f4e21221634e4c24bd69e62d6e110cda2e60b2a17bf',16)
c1=int('0x5f4a7a1c54bd14d1390b6f13a0a366a98f93cb68347a70684d9ce513ba1fb2e3dd72d2e5c73e432658400bc4da175a2bca6861550199337d67a40814461eaa34774a8e7179e1a33b5769946f2d387021e14e814e58bba87d0b9fa8443b8e66c7876c83e8b49d67d92613953afc7b4ce80149e189413f6d44f40460836668ecfd',16)


e2=int('0x2be3fbd6f7db6a8a1f04533cd3ed3f0399d43261dc5abbca04e388724f6f7ec5342f027381cc4a72b4f470ff47a01caa0e70e169c31e46c773f8b23e34683b51746a97f665f8718ca1c2a27581fbb061aa7d03e26de76af4f64788dcf44691a7f397c1fba842184a8571792f239993302b0b33e65359c1d4c4e72c4b36e55775',16)
n2=int('0x7ffdd5a578d58184af984353fed4d55b79fa92113a9f1176af691b8938340b1a7cbdf7501da790c5e899be4d77d9415f8fec271fb07b2249e147136b0823022833a9c8d58f3b6f3bea52f55cc603abb32463583aa1f29a1a9639f09b5e370cda35e1e885db83059a6bf530067bc2f3dd752216495e0d478479dec2b7e0f8dfa3',16)
c2=int('0x28e4ac6fc608d2bb8889f6ea73c07828796cff301c708d1763a139cf57640e254d93c2cdcaf79a0e33db68ebc93f72013065ac554512ab4374fe5edc023c9291bf3615d7932ab471cb4b574913c16c8452b76ad88c3c4b483e686294369577f07cbdc497e6082e1b9313529e112b54b8f5b5b86996ad76898c3315aeebb5036c',16)


M=gmpy2.iroot(int(n2),int(2))[0]
a=[0]*4
a[0]=[M,e0,e1,e2]
a[1]=[0,-n0,0,0]
a[2]=[0,0,-n1,0]
a[3]=[0,0,0,-n2]

Mat = matrix(ZZ,a)
Mat_LLL=Mat.LLL()
d = abs(Mat_LLL[0][0])//M
print(int(d))
m = pow(c2,int(d),n2)
flag = libnum.n2s(int(m))
print(flag)
