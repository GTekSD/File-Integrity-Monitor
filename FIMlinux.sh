

└─$ find * -exec md5sum {} \; > hash_original
                                                                                                                                                            
└─$ find * -exec md5sum {} \; > hash_modefied
                                                                                                                                                             
└─$ diff hash_original hash_modefied

