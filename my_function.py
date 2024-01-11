
    def get_song_ids(df: pd.DataFrame):
    """
    Get the ID of the songs
    """
    import time
    
    list_of_ids = []
    
    # First, we are creating chunks:
    chunk_size = 50
    
    for start in range(0, len(df), chunk_size):
        chunk = df[start:start+chunk_size]
        
        for index, row in chunk.iterrows():
            try:
                #search_song = sp.search(q="tracks:"+df['title'][s]+" artist:"+df['artist'][s],limit=1)
                search_song = sp.search(q=row['title'], limit=1)
                song_id = search_song['tracks']['items'][0]['id']
                list_of_ids.append(song_id)
            
            except:
                print("Song not found!")
                list_of_ids.append("")
                
        print("Sleeping a bit before getting the next ids")
        time.sleep(20)
        
    return list_of_ids
    
    def get_audio_features(list_of_song_ids: list):
    """
    """
    
    import time 
    
    feature_list = []
    
    # First, we are creating chunks:
    chunk_size = 50
    
    for start in range(0, len(list_of_song_ids), chunk_size):
        chunk = list_of_song_ids[start:start+chunk_size]
        
        for i in chunk:
            try:
                my_dict = sp.audio_features([i])[0]
                #my_dict_new = {key : [my_dict[key]] for key in my_dict.keys()}
                feature_list.append(my_dict)
                
            except:
                print("Error retrieving features for song:", i)
    
        print("Sleeping a bit before getting the next ids")
        time.sleep(20)
        
    feature_df = pd.DataFrame(feature_list)
    
    return feature_df
    
    def add_audio_features(df, audio_features_df):
    """
    Concats a given dataframe with the audio features dataframe and return the extended data frame. 
    """
    
    final_df = pd.concat([df, audio_features_df], axis=1)
    
    return final_df
    