

└─$ find *.txt -exec md5sum {} \; > hashmod
                                                                                                                                                            
└─$ find *.txt -exec md5sum {} \; > hashnew
                                                                                                                                                             
└─$ diff hashnew hashmod

