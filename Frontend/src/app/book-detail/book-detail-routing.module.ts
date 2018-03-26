import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';

import {extract} from '@app/core';
import {BookDetailComponent} from './book-detail.component';

const routes: Routes = [
  // Module is lazy loaded, see app-routing.module.ts
  {path: '', component: BookDetailComponent, data: {title: extract('Book-details')}}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
  providers: []
})
export class BookDetailRoutingModule {
}
