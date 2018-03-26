import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {TranslateModule} from '@ngx-translate/core';
import {FlexLayoutModule} from '@angular/flex-layout';

import {MaterialModule} from '@app/material.module';
import {ActivitiesRoutingModule} from './activities-routing.module';
import {ActivitiesComponent} from './activities.component';
import {SharedModule} from '@app/shared';
import {ActivitiesService} from './activities.service';
import {NewBookComponent} from './new-book/new-book.component';
import {UserActivitiesComponent} from './user-activities/user-activities.component';
import {UserActivitiesService} from './user-activities/user-activities.service';
import {NewBookService} from './new-book/new-book.service';
import {FormsModule} from '@angular/forms';
import {ReviewsComponent} from './reviews/reviews.component';
import {ReviewsService} from './reviews/reviews.service';


@NgModule({
  imports: [
    CommonModule,
    TranslateModule,
    FlexLayoutModule,
    MaterialModule,
    SharedModule,
    FormsModule,
    ActivitiesRoutingModule
  ],
  providers: [
    ActivitiesService,
    NewBookService,
    ReviewsService,
    UserActivitiesService


  ],
  declarations: [
    ActivitiesComponent,
    NewBookComponent,
    ReviewsComponent,
    UserActivitiesComponent

  ]
})
export class ActivitiesModule {
}
