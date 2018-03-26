import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';


const routes = {
  reviewsComments: () => `/user/reviews/comments/`,
  reviewsStars: () => `/user/reviews/stars/`
};


@Injectable()
export class ReviewsService {

  constructor(private httpClient: HttpClient) {
  }

  // todo creation date
  getComments(page: string = ''): Observable<any> {

    return this.httpClient
      .get(routes.reviewsComments() + page, {withCredentials: true});
  }

  getStars(page: string = ''): Observable<any> {

    return this.httpClient
      .get(routes.reviewsStars() + page, {withCredentials: true});
  }

}
