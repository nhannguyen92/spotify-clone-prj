from django.urls import path
from music.views import CreateTrack, GetArtistList, GetTopCharts, GetArtistDetailsById, GetSongDetailsById, GetAlbumList, GetTotalAlbums, GetTotalTracks, UpdateTrackViews, GetGenreList, GetSongByGenreID, GetSongBySearchName, DownloadTrack

urlpatterns = [
    path('tracks/<int:track_id>/play/', UpdateTrackViews.as_view(), name='update_track_views'),
    path('topcharts/', GetTopCharts.as_view(), name='get_top_charts'),
    path('tracks/genre/<int:genre_id>/', GetSongByGenreID.as_view(), name='get_songs_by_genre_id'),
    path('genre/', GetGenreList.as_view(), name='get_genre_list'),  
    path('tracks/search/', GetSongBySearchName.as_view(), name='get_songs_by_search'),
    path('artist/details/<int:artist_id>/', GetArtistDetailsById.as_view(), name='get_songs_by_artist_id'),
    path('tracks/tracksdetail/<int:track_id>/', GetSongDetailsById.as_view(), name='get_songs_by_track_id'),
    path('tracks/albums/', GetAlbumList.as_view(), name='get_album_list'),
    path('tracks/download/<int:track_id>/', DownloadTrack.as_view(), name='download_track'),
    path('tracks/create/', CreateTrack.as_view(), name='create_track'),
    path('stats/albums/', GetTotalAlbums.as_view(), name='get_total_albums'),
    path('stats/tracks/', GetTotalTracks.as_view(), name='get_total_tracks'),
    path('artists/', GetArtistList.as_view(), name='get_artist_list'),
]