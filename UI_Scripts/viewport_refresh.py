def main():
     desktop = hou.ui.curDesktop()
     scene_viewer = desktop.paneTabOfType(hou.paneTabType.SceneViewer)
     pane = scene_viewer.pane()
 
     #save current viewport setting
     oldscene = scene_viewer
 
     #save curViewport camera object
     cam = oldscene.curViewport().defaultCamera()
     saved = cam.stash()
 
     #save flipbook setting
     startF,endF = oldscene.flipbookSettings().frameRange()
     use_res = oldscene.flipbookSettings().useResolution()
 
     #create new scene viewer
     scene_viewer = pane.createTab(hou.paneTabType.SceneViewer)
     newscene = scene_viewer
 
     # start restoring flipbook settings to new scene viewer
     # see hou.GeometryViewport class, hou.GeometryViewportCamera class to find methods you need
 
     newscene.flipbookSettings().frameRange((startF,endF))
     newscene.flipbookSettings().useResolution(use_res)
 
     #restore toolbar states
     newscene.setCurrentState(oldscene.currentState())
     newscene.showOperationBar(oldscene.isShowingOperationBar())
     newscene.showSelectionBar(oldscene.isShowingSelectionBar())
     newscene.showDisplayOptionsBar(oldscene.isShowingDisplayOptionsBar())
 
     #restore camera
     #If current viewport has cam selected, it restores it's value
     #if not, current camera data extracted above (cam.stash) will be restored.
     if oldscene.curViewport().camera() is None :
         newscene.curViewport().setDefaultCamera(saved)
     else :
         newscene.curViewport().setCamera(oldscene.curViewport().camera())
 
     #terminate old scene viewer
     oldscene.close()
 
 
main()
