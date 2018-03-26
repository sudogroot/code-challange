import {NgModule} from '@angular/core';
import {Routes, RouterModule, PreloadAllModules} from '@angular/router';
import {Route} from '@app/core';

const routes: Routes = [
  Route.withShell([
    {path: 'activities', loadChildren: 'app/activities/activities.module#ActivitiesModule'},
    {path: 'book/:isbn', loadChildren: 'app/book-detail/book-detail.module#BookDetailModule'},
  ]),
  // Fallback when no prior route is matched
  {path: '**', redirectTo: '', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {preloadingStrategy: PreloadAllModules})],
  exports: [RouterModule],
  providers: []
})
export class AppRoutingModule {
}
