import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {NewBookComponent} from './new-book/new-book.component';
import {UserActivitiesComponent} from './user-activities/user-activities.component';
import {ReviewsComponent} from './reviews/reviews.component';
import {extract} from '@app/core';
import {ActivitiesComponent} from './activities.component';

const routes: Routes = [
  // Module is lazy loaded, see app-routing.module.ts
  {
    path: '',
    data: {title: extract('Activities')},
    children: [
      {
        path: '',
        component: ActivitiesComponent
      },
      {
        path: 'book',
        component: NewBookComponent,

      },
      {
        path: 'history',
        component: UserActivitiesComponent,

      },
      {
        path: 'reviews',
        component: ReviewsComponent,

      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
  providers: []
})
export class ActivitiesRoutingModule {
}
